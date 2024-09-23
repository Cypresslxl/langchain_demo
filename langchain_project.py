from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
from langchain_core.output_parsers import StrOutputParser

# Initialize the ChatOpenAI LLM
openai_api_key = 'sk-4qls0U6W8jZAOANsQ418yHcCBYo8KTgtZ2RV78YUSLT3BlbkFJV15cC6uNFcIdwl_H4FmU78WkIMDgvLMLOqyVE0iicA'
llm = ChatOpenAI(openai_api_key=openai_api_key)

# Initialize chat history
chat_history = ChatMessageHistory()

# Create a chat prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Create a chain using the new method
chain = prompt | llm | StrOutputParser()

# Simulate a conversation
user_input = "Hello, how can I use LangChain?"
response = chain.invoke({"input": user_input, "history": chat_history.messages})

print("AI:", response)

# Store the messages in the history
chat_history.add_user_message(user_input)
chat_history.add_ai_message(response)

# You can continue the conversation by invoking the chain again with new input
# and passing the updated chat_history.messages