import language_model
import asyncio

async def main():
    chat = language_model.LanguageModel("chat-bison@001")
    await chat.start_chat()
    response = await chat.get_response("Hello, How are you?")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
