# Define a class to handle file-related operations
class FuncoesArquivos():
    
    # Constructor method: stores the name/path of the file to be used
    def __init__(self, file_name):
        self.file_name = file_name

    # Method to load the file and return its content as a string
    def load_file(self):
        try:
            # Try to open the file in read mode ('r')
            with open(self.file_name, "r") as f:
                dados = f.read()  # Read the entire file content into a variable
                return dados      # Return the content to the caller

        # Handle the case where the file doesn't exist
        except FileNotFoundError as e:
            print(f"O arquivo nao foi encontrado\n {e}")  # Print error message with details

        # Handle other I/O related errors (e.g., permission issues)
        except IOError as e:
            print(f"Erro no carregamento do arquivo\n {e}")  # Print error message with details
