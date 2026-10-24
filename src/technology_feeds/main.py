from technology_feeds.providers.factory import create_llm_provider

def main() -> None:
    llm = create_llm_provider()
    user_query = input("User query/prompt: ")

    answer = llm.generate(user_query)

    print(answer)

if __name__ == "__main__":
    main()
