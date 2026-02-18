# Microsoft Products Chat Application

A simple, interactive chat application that answers questions about Microsoft products.

## Overview

This chat application provides information about various Microsoft products including Windows, Microsoft 365, Azure, Visual Studio, Teams, SQL Server, Power BI, Dynamics 365, Xbox, and Edge. Users can ask questions naturally and get detailed information about features, use cases, and versions.

## Features

- **Interactive Chat Interface**: Natural language interaction to ask about Microsoft products
- **Comprehensive Knowledge Base**: Information about 10+ major Microsoft products
- **Smart Search**: Finds relevant products based on keywords and context
- **Product Details**: Provides descriptions, key features, latest versions, and use cases
- **Easy Commands**: Simple commands for listing products and getting help

## Installation

### Prerequisites
- Python 3.7 or higher

### Setup

1. Clone the repository:
```bash
git clone https://github.com/AjinkyaPawale1/AIDevops.git
cd AIDevops
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the chat application:

```bash
python chat_app.py
```

### Available Commands

- **Ask questions naturally**: "What is Azure?", "Tell me about Windows", "Show me collaboration tools"
- **`list`**: Display all available Microsoft products
- **`help`**: Show help message and usage instructions
- **`quit` or `exit`**: Exit the application

### Example Interactions

```
You: What is Azure?
[Displays detailed information about Microsoft Azure]

You: Tell me about collaboration tools
[Shows Microsoft Teams and Microsoft 365]

You: list
[Lists all available Microsoft products]

You: Tell me about Windows
[Displays detailed information about Windows]
```

## Supported Microsoft Products

1. **Windows** - Operating system
2. **Microsoft 365** - Office productivity suite
3. **Azure** - Cloud computing platform
4. **Visual Studio** - Integrated development environment
5. **Teams** - Collaboration platform
6. **SQL Server** - Database management system
7. **Power BI** - Business analytics service
8. **Dynamics 365** - CRM and ERP applications
9. **Xbox** - Gaming platform
10. **Edge** - Web browser

## Project Structure

```
AIDevops/
├── chat_app.py          # Main chat application
├── knowledge_base.py    # Microsoft products knowledge base
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to add more Microsoft products or improve the chat experience.

## License

This project is open source and available for educational purposes.

## Future Enhancements

- Integration with OpenAI API for more natural conversations
- Web-based interface
- More detailed product information
- Product comparison features
- Links to official Microsoft documentation