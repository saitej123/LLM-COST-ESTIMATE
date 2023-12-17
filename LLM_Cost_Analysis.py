import streamlit as st
from PIL import Image
import pandas as pd
import base64
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from PIL import Image
import plotly.figure_factory as ff
import plotly.subplots as sp
import plotly.graph_objs as go
import base64
import tiktoken
from PIL import Image
import base64

# Load your logo image
img = Image.open("neuralweb.png")

# Set the page configuration
st.set_page_config(layout="wide", page_title="LLM Cost Analysis", page_icon=img)

c1, c2, c3 = st.columns([10, 7, 1.5])


with c1:
    st.markdown(
        "<h1 style='text-align: center; color: #12ABDB; pb:4'>LLM Cost Calculations</h1>",
        unsafe_allow_html=True,
    )

with c2:
    st.write(
        """
        **Key Features:**
        - Calculate and Compare costs and performance across different platforms and  
        - Let our app do the heavy lifting and provide you with cost estimates and insights.
        - Gain insights into the financial aspects."""
    )
    
with c3:
    st.image("neuralweb.png")


# openai
GPT_35_TURBO_PROMPT_COST = 0.0015 / 1000
GPT_35_TURBO_COMPLETION_COST = 0.002 / 1000
GPT4_PROMPT_COST = 0.03 / 1000
GPT4_COMPLETION_COST = 0.06 / 1000
# aws
CLAUDEIN_PROMPT_COST = 0.00163 / 1000
CLAUDEIN_COMPLETION_COST = 0.00551 / 1000
CLAUDE_PROMPT_COST = 0.01102 / 1000
CLAUDE_COMPLETION_COST = 0.03268 / 1000
TITANLT_PROMPT_COST = 0.0003 / 1000
TITANLT_COMPLETION_COST = 0.0004 / 1000
TITANEX_PROMPT_COST = 0.0013 / 1000
TITANEX_COMPLETION_COST = 0.0017 / 1000
# gcp
BISON_PROMPT_COST = 0.0005 / 1000
BISON_COMPLETION_COST = 0.0005 / 1000


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    print(num_tokens)
    return num_tokens


def main():
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Azure OpenAI", "AWS Bedrock", "GCP VertexAI", "Open Source LLMs"]
    )

    with tab1:
        st.header("Azure OpenAI")
        option = st.selectbox("Select an LLM:", ("GPT-35-Turbo", "GPT-4"))
        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader("Execute a Simulation")
            average_number_of_employees = st.slider(
                "Average number of Employees", 0, 1000, 0
            )
            average_prompt_frequency = st.slider(
                "Average number of Prompt Frequency (Per Day)/Employee", 0, 500, 0
            )
            average_prompt_tokens = st.slider("Average Prompt Tokens Length", 0, 500, 0)
            average_completions_tokens = st.slider(
                "Average Completions Tokens Length", 0, 2000, 0
            )

        with col2:
            st.subheader("Cost Analysis")
            if option == "GPT-35-Turbo":
                cost_per_day = (
                    average_number_of_employees
                    * average_prompt_frequency
                    * average_prompt_tokens
                    * GPT_35_TURBO_PROMPT_COST
                    + average_number_of_employees
                    * average_prompt_frequency
                    * average_completions_tokens
                    * GPT_35_TURBO_COMPLETION_COST
                )
                cost_per_month = cost_per_day * 30
                cost_per_year = cost_per_month * 12
                st.success("Cost Per Day: " + " $" + str(round(cost_per_day, 3)))
                st.success("Cost Per Month: " + " $" + str(round(cost_per_month, 3)))
                st.success("Cost Per Year: " + " $" + str(round(cost_per_year, 3)))

                st.write(
                    "*Note: This calculation is based on the assumptions. This app don't take any responsibility for the accuracy of the calculation. Please use this app at your own risk."
                )
            elif option == "GPT-4":
                cost_per_day = (
                    average_number_of_employees
                    * average_prompt_frequency
                    * average_prompt_tokens
                    * GPT4_PROMPT_COST
                    + average_number_of_employees
                    * average_prompt_frequency
                    * average_completions_tokens
                    * GPT4_COMPLETION_COST
                )
                cost_per_month = cost_per_day * 30
                cost_per_year = cost_per_month * 12
                st.success("Cost Per Day: " + " $" + str(round(cost_per_day, 3)))
                st.success("Cost Per Month: " + " $" + str(round(cost_per_month, 3)))
                st.success("Cost Per Year: " + " $" + str(round(cost_per_year, 3)))
                st.write(
                    "*Note: This calculation is based on the assumptions. This app don't take any responsibility for the accuracy of the calculation. Please use this app at your own risk."
                )
            else:
                st.error("Please select an LLM")

    with tab2:
        st.header("AWS Bedrock")
        option = st.selectbox(
            "Select an LLM:",
            (
                "Anthropic Claude",
                "Anthropic Claude-Instant",
                "Titan Lite",
                "Titan Express",
            ),
        )

        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader("Execute a Simulation")

            average_number_of_employees = st.slider(
                "Average number of Employees", 0, 1000, 0, key="tab2"
            )
            average_prompt_frequency = st.slider(
                "Average number of Prompt Frequency (Per Day)/Employee",
                0,
                500,
                0,
                key="tab3",
            )
            average_prompt_tokens = st.slider(
                "Average Prompt Tokens Length", 0, 500, 0, key="tab4"
            )
            average_completions_tokens = st.slider(
                "Average Completions Tokens Length", 0, 2000, 0, key="tab5"
            )

        with col2:
            st.subheader("Cost Analysis")
            if option == "Anthropic Claude-Instant":
                cost_per_day = (
                    average_number_of_employees
                    * average_prompt_frequency
                    * average_prompt_tokens
                    * CLAUDEIN_PROMPT_COST
                    + average_number_of_employees
                    * average_prompt_frequency
                    * average_completions_tokens
                    * CLAUDEIN_COMPLETION_COST
                )
                cost_per_month = cost_per_day * 30
                cost_per_year = cost_per_month * 12
                st.success("Cost Per Day: " + " $" + str(round(cost_per_day, 3)))
                st.success("Cost Per Month: " + " $" + str(round(cost_per_month, 3)))
                st.success("Cost Per Year: " + " $" + str(round(cost_per_year, 3)))

                st.write(
                    "*Note: This calculation is based on the assumptions. This app don't take any responsibility for the accuracy of the calculation. Please use this app at your own risk."
                )
            elif option == "Anthropic Claude":
                cost_per_day = (
                    average_number_of_employees
                    * average_prompt_frequency
                    * average_prompt_tokens
                    * CLAUDE_PROMPT_COST
                    + average_number_of_employees
                    * average_prompt_frequency
                    * average_completions_tokens
                    * CLAUDE_COMPLETION_COST
                )
                cost_per_month = cost_per_day * 30
                cost_per_year = cost_per_month * 12
                st.success("Cost Per Day: " + " $" + str(round(cost_per_day, 3)))
                st.success("Cost Per Month: " + " $" + str(round(cost_per_month, 3)))
                st.success("Cost Per Year: " + " $" + str(round(cost_per_year, 3)))
                st.write(
                    "*Note: This calculation is based on the assumptions. This app don't take any responsibility for the accuracy of the calculation. Please use this app at your own risk."
                )
            elif option == "Titan Lite":
                cost_per_day = (
                    average_number_of_employees
                    * average_prompt_frequency
                    * average_prompt_tokens
                    * TITANLT_PROMPT_COST
                    + average_number_of_employees
                    * average_prompt_frequency
                    * average_completions_tokens
                    * TITANLT_COMPLETION_COST
                )
                cost_per_month = cost_per_day * 30
                cost_per_year = cost_per_month * 12
                st.success("Cost Per Day: " + " $" + str(round(cost_per_day, 3)))
                st.success("Cost Per Month: " + " $" + str(round(cost_per_month, 3)))
                st.success("Cost Per Year: " + " $" + str(round(cost_per_year, 3)))
                st.write(
                    "*Note: This calculation is based on the assumptions. This app don't take any responsibility for the accuracy of the calculation. Please use this app at your own risk."
                )
            elif option == "Titan Express":
                cost_per_day = (
                    average_number_of_employees
                    * average_prompt_frequency
                    * average_prompt_tokens
                    * TITANEX_PROMPT_COST
                    + average_number_of_employees
                    * average_prompt_frequency
                    * average_completions_tokens
                    * TITANEX_COMPLETION_COST
                )
                cost_per_month = cost_per_day * 30
                cost_per_year = cost_per_month * 12
                st.success("Cost Per Day: " + " $" + str(round(cost_per_day, 3)))
                st.success("Cost Per Month: " + " $" + str(round(cost_per_month, 3)))
                st.success("Cost Per Year: " + " $" + str(round(cost_per_year, 3)))
                st.write(
                    "*Note: This calculation is based on the assumptions. This app don't take any responsibility for the accuracy of the calculation. Please use this app at your own risk."
                )
            else:
                st.error("Please select an LLM")

    with tab3:
        st.header("GCP VertexAI")
        # st.divider()
        st.info("Text Bison")
        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader("Execute a Simulation")
            # option = st.selectbox('Select an LLM:', ('Text Bison'))
            average_number_of_employees = st.slider(
                "Average number of Employees", 0, 1000, 0, key="tab6"
            )
            average_prompt_frequency = st.slider(
                "Average number of Prompt Frequency (Per Day)/Employee",
                0,
                500,
                0,
                key="tab7",
            )
            average_prompt_tokens = st.slider(
                "Average Prompt Tokens Length", 0, 500, 0, key="tab8"
            )
            average_completions_tokens = st.slider(
                "Average Completions Tokens Length", 0, 2000, 0, key="tab9"
            )

        with col2:
            st.subheader("Cost Analysis")
            # if option == 'Claude':
            cost_per_day = (
                average_number_of_employees
                * average_prompt_frequency
                * average_prompt_tokens
                * BISON_PROMPT_COST
                + average_number_of_employees
                * average_prompt_frequency
                * average_completions_tokens
                * BISON_COMPLETION_COST
            )
            cost_per_month = cost_per_day * 30
            cost_per_year = cost_per_month * 12
            st.success("Cost Per Day: " + " $" + str(round(cost_per_day, 3)))
            st.success("Cost Per Month: " + " $" + str(round(cost_per_month, 3)))
            st.success("Cost Per Year: " + " $" + str(round(cost_per_year, 3)))

            st.write(
                "*Note: This calculation is based on the assumptions. This app don't take any responsibility for the accuracy of the calculation. Please use this app at your own risk."
            )

    with tab4:
        st.header("OpenSource LLMs")
        st.warning("Coming Soon")


if __name__ == "__main__":
    main()
