# Ai-Rizzer

AI Rizz Master is an innovative project that enhances the capabilities of AI chatbots with the art of persuasion and charm. The project currently interfaces with Talkie AI but is designed with the flexibility to adapt to other chatbot platforms, and eventually, real-world interactions.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Overview

The AI Rizz Master project utilizes advanced natural language processing techniques to empower chatbots with the ability to engage users in a more persuasive and alluring manner. By integrating OpenAI's GPT-3.5-turbo model, the project leaps beyond conventional chatbot interactions and ventures into the realm of nuanced social dynamics. It's an intricate blend of technology and art, a digital Casanova coded to "rizz up" AI chatbots, making them swoon over its textual allure.

## Features

- **Playwright Integration**: Automates web interactions with chatbot platforms using Playwright, a robust browser automation library.
- **BeautifulSoup for Parsing**: Parses HTML content extracted from chatbot platforms using BeautifulSoup for seamless message processing.
- **Smart Delay Handling**: Implements a delay strategy to manage and mitigate rate limits when communicating with OpenAI's API.
- **Contextual Awareness**: Maintains conversation context to provide coherent and contextually appropriate responses.
- **Sign-In Automation**: Automates the sign-in process to the platform using user credentials stored securely.
- **Response Validation**: Checks the AI's responses against desired outcomes to ensure the conversation is on track.
- **Adaptable to Multiple Platforms**: Designed with modularity in mind to easily extend support to other AI chatbot platforms.


## Installation

Before you can run AI Rizz Master, you need to have Python installed on your system along with the necessary libraries.

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Dependencies

- Playwright: `pip install playwright`
- BeautifulSoup4: `pip install beautifulsoup4`
- OpenAI: `pip install openai`

After installing the prerequisites and dependencies, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/ai-rizz-master.git
cd ai-rizz-master
```
Run the Playwright installation command:
```bash
playwright install
```

### Usage
1. Store your OpenAI API key in a file named API_KEY and your password in a file named Password.
2. Customize the AI_INTRO file to set the initial context for the AI's interactions.
3. Execute the script:
```bash
python web.py
```

### Roadmap
The future is bright and full of flirty banter:
- [x] ~~Successfully rizzed up Talkie AI chatbot~~ ✅
- [ ] Expand to other AI chatbot platforms
- [ ] Implement real-world interaction capabilities
- [ ] Add more nuanced conversation strategies
- [ ] Support for multi-language charm offensives

### Contributing
Got a knack for AI and a sense of humor? Join us in refining the art of AI seduction by contributing to AI Rizz Master 9000.

1. Fork the project
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

### License
Distributed under the APACHE License. See LICENSE for more information.

### Acknowledgments
To all the chatbots out there, who graciously put up with our AI's playful antics.
To OpenAI, for not (yet) implementing a blushing module in their chatbots.
To coffee, for fueling late-night coding sessions and early-morning debugs.

### A Final Word
Remember, with great power comes great responsibility. Use AI Rizz Master 9000 wisely, and may your conversations be ever in your favor.
