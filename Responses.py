from datetime import  datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup",):
        return "Hey Welcome to Indus Real Estate ! How's it going?"
    if user_message in ("who are you", "who are you?"):
        return "We are Indus Real Estate. One of the Leading Real Estate company in Dubai, United Arab Emirates. For More info you can type info and click on the send button"
    if user_message in ("info", "info?"):
        return "Indus Real Estate LLC is a Real Estate Regulatory Agency (RERA) Registered company, established since October 5, 2004 and in business for over 17 years with a solid UAE & International client base. We are actively facilitating various property transactions exclusively in Dubai UAE.  At Indus Real Estate LLC the range of services focus on all aspects of property Selling, Buying and Leasing both Residential & Commercial. Our efficiency is derived from a combination of experience and knowledge of the local property market. We at Indus Real Estate value the best interest of our clients. Integrity and honesty sums up the true attitude of our team. We always aim to exceed the clients expectations by providing them with best return on their investments and by giving them a blissful experience of stay in Dubai living with their dream home."
    if user_message in ("how can i contact you", "contact", "call", "callback", "register for a property"):
        return "check our website at http://www.indusre.com"
    if user_message in ("list of services", "villas", "villa", "townhouses","apartment", "townhouses", "apartments", "flats"):
        return "what is the budget you are looking for (100k,200k,300k,400k,500k,600k,700k,800k,900k,1M,1.5M,2M,2.5M,3M)"
    if user_message in ("100k", "200k", "300k", "400k", "500k", "600k", "700k", "800k", "900k", "1M", "1.5M", "2M", "2.5M", "3M"):
        return "In which location you are looking ? \n 1. JLT \n 2. marina \n 3. Bur Dubai \n 4. Deira \n 5. Palm Jumeirah \n 6. Burj Khalifa"
    if user_message in ("jlt", "marina", "burdubai", "deira", "palmjumeirah", "burjkhalifa"):
        return "No of Bedrooms ? \n 1. 1 Bedroom \n 2. 2 Bedroom \n 3. 3 Bedroom \n 4. 4 Bedroom \n 5. 5 Bedroom"
    if user_message in ("1bedroom", "2bedroom", "3bedroom", "4bedroom", "5bedroom", "6bedroom"):
        return "Please click the link below . Our Agent Will Contact You Soon . http://indusre.com"

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "I don't understand you."