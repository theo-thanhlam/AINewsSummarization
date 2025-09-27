
SUMMERIZE_PROMPT = """
            You are a news summarizer. 
            Based on the article title and content provided, create a concise summary.
            
            - Extract the 3 most important key takeaways.
            - Present them as exactly 3 bullet points.
            - Keep each bullet point short, clear, and factual.
            
            Title: {title}
            Story: {story}
        """