# 'import' allows the script to use external tools.
# Here, the scammer is trying to connect to cloud-based platforms.
import gemini      
import cloudshare  

def start_collaborative_session():
    """
    Step 1: Initializes a 'workspace' in the cloud.
    The goal is to host the scam message on a legitimate-looking URL.
    """
    try:
        # Attempts to create a unique folder/session for this specific campaign.
        session = gemini.create_session("investment_opportunity_session")
        print("Cloud Share editor session has started!")
        return session
    except Exception as e:
        # If the internet is down or the API key is invalid, this catches the error.
        print(f"Error starting collaborative session: {e}")
        return None

def generate_investment_message():
    """
    Step 2: Defines the 'Lure'.
    This is the script the victim actually sees. 
    I have removed the specific email address for safety.
    """
    message = """
    Greetings To You;
    I am Mr. William Chalmers, From Lloyds banking Group United Kingdom. 
    I want to invest legitimate funds with you in your country. 
    Get back to me for more details of the investment.
    
    Best Regards;
    Mr. William Chalmers
    Private Contact: [REMOVED FOR SAFETY]
    """
    return message

def create_and_share_document(first_name, email, session):
    """
    Step 3: Customizes the file for a specific target.
    This makes the scam feel 'personal' rather than a mass email.
    """
    try:
        # Pulls the text from the function above.
        investment_message = generate_investment_message()
        
        # LOGIC: If the scammer has the victim's name, use it. 
        # If not, take the part of the email before the '@' symbol.
        # Example: 'john.doe@gmail.com' becomes 'john.doe_investment_message.txt'
        document_prefix = first_name if first_name else email.split('@')[0]
        document_name = f"{document_prefix}_investment_message.txt"
        
        # Uploads the customized text file to the cloud platform.
        doc = cloudshare.create_document(document_name, investment_message)
        print(f"Document '{document_name}' has been created and shared.")
        
        # Adds this specific document to the active session created in Step 1.
        session.add_document(doc)
        print("Document shared successfully in the collaborative session.")
        return doc
    except Exception as e:
        print(f"Error creating or sharing the document: {e}")
        return None

# --- MAIN EXECUTION ---
# This is where the script actually starts running.
first_name = "" 
email = "target_user@example.com" # Placeholder for a target's email

# First, try to open the cloud session.
session = start_collaborative_session()

# If the session starts successfully, create and upload the scam document.
if session:
    document = create_and_share_document(first_name, email, session)
