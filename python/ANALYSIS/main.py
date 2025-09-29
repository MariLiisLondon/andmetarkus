
from file_functions import FileFunctions  

def main():
    """Main function to read and print the content of a log file, and add a new line at the end."""
    
    failitee = r"C:\Users\opilane\Documents\andmetarkus-1\python\ANALYSIS\request-log.txt"
    
   
    # request_log_entries = filecontent.split("\n")

    request_log_entries = FileFunctions().read_file(failitee)

    for line in request_log_entries:
        print(line + "\n")

    row_count = len(request_log_entries)
    print(f"Logifailis on {row_count} rida.")

    FileFunctions().add_line_to_file(
        failitee, f"Logifailis on {row_count} rida.")


if __name__ == "__main__":
    main()






    

