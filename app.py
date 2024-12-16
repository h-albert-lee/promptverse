import streamlit as st
from backend import database, prompt_manager, application_manager, dataset_manager, evaluation, yaml_manager, auth

database.initialize_database()

# Authentication
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    st.title("Login to LLMOps Tool")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if auth.authenticate_user(username, password):
            st.session_state['authenticated'] = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")
else:
    # Main App Menu
    st.title("LLMOps Tool")
    menu = st.sidebar.selectbox("Menu", ["Prompts", "Applications", "Datasets", "Evaluation", "YAML Management", "Logout"])

    if menu == "Prompts":
        st.header("Prompt Management")
        content = st.text_area("Prompt Content")
        version = st.number_input("Version", min_value=1, step=1)
        if st.button("Create Prompt"):
            prompt_manager.create_prompt(content, version)
            st.success("Prompt Created!")

        # Display active prompts
        st.subheader("Active Prompt")
        conn = sqlite3.connect("llmops.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM prompts WHERE is_active = 1")
        active_prompt = cursor.fetchone()
        conn.close()
        if active_prompt:
            st.write(f"Active Prompt: ID {active_prompt[0]}, Version {active_prompt[1]}, Content: {active_prompt[2]}")

        # Display prompt history
        st.subheader("Prompt History")
        if active_prompt:
            history = prompt_manager.get_prompt_history(active_prompt[0])
            for record in history:
                st.write(f"Version {record[2]}: {record[3]} (Timestamp: {record[4]})")

    if menu == "Applications":
        st.header("Application Management")
        prompt_id = st.number_input("Prompt ID", min_value=1, step=1)
        model_options = st.text_input("Model Options")
        if st.button("Create Application"):
            application_manager.create_application(prompt_id, model_options)
            st.success("Application Created!")

    if menu == "Datasets":
        st.header("Dataset Management")
        name = st.text_input("Dataset Name")
        data = st.text_area("Dataset Content")
        if st.button("Create Dataset"):
            dataset_manager.create_dataset(name, data)
            st.success("Dataset Created!")

    if menu == "Evaluation":
        st.header("Evaluation")
        prompt = st.text_area("Prompt")
        input_text = st.text_area("Input Text")
        if st.button("Call API"):
            result = evaluation.call_api(prompt, input_text)
            st.json(result)

    if menu == "YAML Management":
        st.header("YAML Management")
        yaml_file_path = st.text_input("YAML File Path")
        prompt_content = st.text_area("Prompt Content for YAML")
        if st.button("Write to YAML"):
            yaml_manager.write_prompt_to_yaml(yaml_file_path, prompt_content)
            st.success(f"Prompt written to {yaml_file_path}")

        if st.button("Read from YAML"):
            content = yaml_manager.read_prompt_from_yaml(yaml_file_path)
            st.text_area("Read Content", value=content, height=200)

    if menu == "Logout":
        st.session_state['authenticated'] = False
        st.experimental_rerun()
