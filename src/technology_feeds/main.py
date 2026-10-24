from technology_feeds.providers.factory import create_llm_provider

def main() -> None:
    llm = create_llm_provider()

    answer = llm.generate("Explain in short what an AI agent is in simple words")

    print(answer)

if __name__ == "__main__":
    main()
