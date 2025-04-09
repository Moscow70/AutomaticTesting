class KatalonScriptProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_script(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                script_content = file.read()
            return script_content
        except FileNotFoundError:
            print(f"The file {self.file_path} does not exist.")
            return None
        except Exception as e:
            print(f"An error occurred while reading the script: {e}")
            return None

    def save_processed_script(self, processed_content, output_file_path):
        try:
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(processed_content)
            print(f"Processed script saved to {output_file_path}")
        except Exception as e:
            print(f"An error occurred while saving the script: {e}")