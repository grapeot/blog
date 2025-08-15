Title: When AI Fails: How I Eventually Automated My Personal Finances
Date: 2025-08-14 22:00
Category: Computing
Tags: AI, Machine Learning, English
Slug: ai-finance-en

## A Decade-Long Manual Process

For the past ten years, I've reconciled my personal finances every month. The process was entirely manual: I'd log into multiple bank and brokerage websites, and one by one, enter the name, current value, and date of every stock, bond, fund, and CD into a makeshift Excel spreadsheet. This spreadsheet would generate a summary view, showing my total assets, liabilities, and the distribution of my assets, giving me a complete financial overview.

While useful, this process was a huge pain. It was time-consuming, repetitive, and filled with tedious data entry and calculations where mistakes were easy to make. Surprisingly, I never thought about automating it. Maybe I subconsciously believed it was impossible—accessing multiple closed financial systems just didn't seem technically feasible. But recently, I've used AI to do things I never imagined possible, which led me to rethink this problem: Could I hand this tedious task over to a machine for a more effortless, accurate, and even more frequent financial check-up?

## First Attempt: The Plaid Compliance Wall

My first instinct was to ask an AI assistant for a solution. It suggested a standard, programmatic approach: a tool called Plaid. Plaid is a professional financial services API that allows apps to securely connect to users' bank accounts and retrieve information in a unified format. TurboTax, for example, uses Plaid to gather various tax forms. After learning this, I thought, "Wow, this is amazing." I could use a single API to get all my account holdings and prices. Problem solved.

I immediately applied for a developer account but quickly hit a major roadblock: compliance review. Plaid has a ton of stringent requirements for users applying for a production API key. They sent me a long questionnaire asking things like, "Does your company have a dedicated information security team?", "How often are system patches updated?", "Do you have an internal network vulnerability scanning mechanism?", and "What is your emergency response plan for customer data breaches?" I was floored. I'm just one person trying to connect to my own accounts to check my balances. Why all the shouting?

After hastily filling it out, my application for a production key was quickly rejected. I couldn't use a development key either, because many large banks (like Wells Fargo and Chase) require OAuth for authentication, which in turn requires a production key. This path was a dead end.

## A Change in Strategy: The GUI as the Last API

With the standard data interface blocked, I had to get creative. If full automation wasn't an option, what about semi-automation? My main pain point was manual data entry. If I could solve that, I could still dramatically improve efficiency.

That's when I thought of Vision LLMs and tools like Computer Use. My new approach was this: if I couldn't get the data directly through an API, I'd grab it from the GUI. The workflow would be: I manually log into my bank's website and take screenshots of my holdings. These screenshots contain all the information I need: ticker symbols, prices, total values, etc. Then, I feed these images to a vision large language model (VLLM) for recognition and parsing, converting the unstructured information into a structured JSON/CSV format. Finally, a simple Python script processes this structured data.

I quickly ran an experiment. I chose a locally deployed Ollama environment and used the Qwen2.5-VL:32b model to process the screenshots. The results were excellent. For the 20+ holdings I provided, the model's recognition accuracy was nearly 100%. The only mistake was with the number of shares for one holding—my Microsoft stock had a weirdly fractional share count that the model couldn't handle. It was a minor issue; I could just sell the fractional share. This probing experiment resolved the biggest uncertainty and proved this path was viable.

## Building and Verifying: Can You Trust AI with Financial Data?

With a viable plan, the next step was implementation. But another obstacle emerged: financial data is extremely sensitive. How could I ensure the AI's processing was accurate? In other words, how could I build trust in the AI's results? To solve this, I designed a human-in-the-loop workflow and established a dual-verification framework.

### AI-Assisted Development

First, I used AI for the heavy lifting:

1.  **Data Structure Design:** I had an AI analyze my decade's worth of Excel spreadsheets and design a more standardized and robust database schema (ultimately stored as a simple CSV file for easy analysis by other AIs).
2.  **Prompt Engineering:** Based on this new data structure, I had an AI design a specialized prompt for the VLLM. This prompt guides the model to output highly uniform JSON that can be directly parsed by downstream programs. (The prompt is included at the end of this post.)
3.  **Code Generation:** I had an AI write the Python script for post-processing. This script parses the JSON output from the VLLM, merges it with historical data, and generates a visual HTML report for my review.

The entire workflow is: I take screenshots manually, the local Qwen2.5-VL model processes them and generates JSON files. Then, another script parses the JSON, integrates the data, and creates a visualization. If I review the HTML report and everything looks good, I simply type "yes" in the command line, and the new data is appended to my main database.

### Results-Driven Cross-Validation

My core principle for the AI system's accuracy is to be results-driven, not process-driven. I don't care about the AI's internal thought process or if the program is perfect; I only care if the final output is correct. If, for instance, the AI is correct on 20 out of 20 results with no obvious pattern of error, I assume its accuracy is trustworthy and generalizable.

For validating the results, I used a cross-check method. In my old manual process, I spent a lot of time verifying the total assets each month, so that figure served as a reliable ground truth. My verification method was to use a deterministic program to sum up the values of all individual assets parsed by the AI and compare it to my recorded total for that month. If the difference exceeded 5%, the program would raise an alarm.

After the AI converted my last ten years of Excel records, it found that the error margin for most months was within 5%. However, for six months, the discrepancy was significantly higher. I reviewed these six records one by one and found that almost all the errors were from my original manual entry—either typos in the amounts or incorrect dates causing misalignments. This was an interesting discovery: the automated process not only avoided making new mistakes but also helped me find hidden errors from a decade of manual bookkeeping, further proving the value of automation.

## Conclusion and Reflections

This project took me about two hours and automated a manual task that had plagued me for ten years. Now, I can do in minutes what used to take over half an hour. More importantly, the accuracy and frequency of my financial analysis have improved dramatically.

This experience also left me with a few thoughts:

1.  **The line between GUI and API is blurrier than we think:** When an API is inaccessible due to compliance, commercial, or other reasons, VLLMs offer a new way to automate. Any software's GUI can be treated as an unofficial API, opening up huge possibilities for automating closed, legacy systems.
2.  **The value of local models:** For handling private data, especially financial data, running a model locally with Ollama gave me significant peace of mind. All my sensitive information stays on my own device.
3.  **When full automation fails, try semi-automation:** When AI doesn't seem to work, it's worth taking a step back to remember your original goal. What tradeoffs are you willing to accept? How can you work around the problem? You can think it through yourself or discuss it with an AI. This collaborative mindset can greatly increase your success rate when using AI to complete tasks.

Also, here is the VLLM prompt I used:

---

I'm working on my financial reconciliation and need to convert screenshots of my financial accounts into a standardized JSON format.

**Important Instructions:**

-   Please keep the original monetary values; do not perform any unit conversions.
-   Output only the JSON, with no additional explanatory text.
-   If a field cannot be determined, use a `null` value.

**Output Format Requirements:**

Depending on the screenshot type, output one of the following JSON structures:

### 1. Account List Screenshot
```json
{
  "data_type": "accounts",
  "currency": "USD",
  "items": [
    {
      "name": "[Full Account Name]",
      "balance": "[Balance amount, keep original value]",
      "account_type": "[Account type: checking, savings, brokerage, ira, investment]",
      "account_number_suffix": "[Last few digits of account number]",
      "full_account_name": "[Full account name as shown in the screenshot]"
    }
  ]
}
```

### 2. Stock List Screenshot
```json
{
  "data_type": "stocks",
  "currency": "USD",
  "items": [
    {
      "ticker": "[Stock Ticker]",
      "amount": "[Number of shares, integer]",
      "balance": "[Total value, keep original value]",
      "price_per_share": "[Price per share, if visible]",
      "account_context": "[Associated account info, if visible]"
    }
  ]
}
```

**Account Type Identification Rules:**

-   Contains "checking" → "checking"
-   Contains "savings" → "savings"
-   Contains "brokerage" → "brokerage"
-   Contains "IRA" → "ira"
-   Betterment account → "investment"
-   Other investment accounts → "investment"

Please strictly follow the above format when processing the screenshot content.

---