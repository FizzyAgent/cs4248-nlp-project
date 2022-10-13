from data_generation.data_generator import create_email_data

if __name__ == "__main__":
    email_prompt, email, summarized_points = create_email_data(gen_func=lambda x: "Write your own damn email!")
    print("Prompt:\n", email_prompt)
    print(email)
    print("\n=====\n")
    print("Summary:\n", summarized_points)
