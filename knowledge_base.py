"""
Microsoft Products Knowledge Base
Contains information about various Microsoft products
"""

MICROSOFT_PRODUCTS_KB = {
    "Windows": {
        "description": "Microsoft Windows is a family of operating systems developed by Microsoft. It's the most widely used desktop operating system in the world.",
        "key_features": [
            "User-friendly graphical interface",
            "Wide software compatibility",
            "Regular security updates",
            "Built-in security features like Windows Defender"
        ],
        "latest_version": "Windows 11",
        "use_cases": "Desktop computing, enterprise environments, gaming, and general productivity"
    },
    "Microsoft 365": {
        "description": "Microsoft 365 (formerly Office 365) is a cloud-based subscription service that includes Office applications, cloud storage, and collaboration tools.",
        "key_features": [
            "Word, Excel, PowerPoint, Outlook",
            "OneDrive cloud storage (1TB+)",
            "Microsoft Teams for collaboration",
            "Regular updates and new features"
        ],
        "latest_version": "Microsoft 365 (continuous updates)",
        "use_cases": "Office productivity, document creation, team collaboration, email management"
    },
    "Azure": {
        "description": "Microsoft Azure is a cloud computing platform offering services for building, deploying, and managing applications through Microsoft-managed data centers.",
        "key_features": [
            "Virtual machines and containers",
            "AI and machine learning services",
            "Database and storage solutions",
            "DevOps and developer tools"
        ],
        "latest_version": "Azure (continuous updates)",
        "use_cases": "Cloud infrastructure, application hosting, AI/ML workloads, enterprise IT solutions"
    },
    "Visual Studio": {
        "description": "Visual Studio is an integrated development environment (IDE) from Microsoft for developing applications for Windows, web, mobile, and cloud platforms.",
        "key_features": [
            "Advanced code editor with IntelliSense",
            "Built-in debugger",
            "Support for multiple programming languages",
            "Integration with Azure and GitHub"
        ],
        "latest_version": "Visual Studio 2022",
        "use_cases": "Software development, web development, mobile app development, game development"
    },
    "Teams": {
        "description": "Microsoft Teams is a collaboration platform that combines workplace chat, video meetings, file storage, and application integration.",
        "key_features": [
            "Video and audio conferencing",
            "Chat and instant messaging",
            "File sharing and collaboration",
            "Integration with Microsoft 365"
        ],
        "latest_version": "Microsoft Teams (continuous updates)",
        "use_cases": "Remote work, team collaboration, virtual meetings, project management"
    },
    "SQL Server": {
        "description": "Microsoft SQL Server is a relational database management system (RDBMS) designed for enterprise environments.",
        "key_features": [
            "High performance and scalability",
            "Advanced security features",
            "Business intelligence tools",
            "Support for cloud and on-premises deployment"
        ],
        "latest_version": "SQL Server 2022",
        "use_cases": "Enterprise databases, data warehousing, business intelligence, analytics"
    },
    "Power BI": {
        "description": "Power BI is a business analytics service that provides interactive visualizations and business intelligence capabilities.",
        "key_features": [
            "Interactive data visualization",
            "Custom dashboards and reports",
            "Integration with multiple data sources",
            "AI-powered insights"
        ],
        "latest_version": "Power BI (continuous updates)",
        "use_cases": "Data analysis, business intelligence, reporting, data visualization"
    },
    "Dynamics 365": {
        "description": "Dynamics 365 is a suite of enterprise resource planning (ERP) and customer relationship management (CRM) applications.",
        "key_features": [
            "CRM and ERP capabilities",
            "Sales and marketing automation",
            "Customer service tools",
            "AI-driven insights"
        ],
        "latest_version": "Dynamics 365 (continuous updates)",
        "use_cases": "Customer relationship management, sales automation, business operations, finance management"
    },
    "Xbox": {
        "description": "Xbox is Microsoft's gaming brand, including gaming consoles, services, and gaming subscription services.",
        "key_features": [
            "High-performance gaming hardware",
            "Xbox Game Pass subscription",
            "Cloud gaming with Xbox Cloud Gaming",
            "Backward compatibility"
        ],
        "latest_version": "Xbox Series X/S",
        "use_cases": "Gaming, entertainment, streaming"
    },
    "Edge": {
        "description": "Microsoft Edge is a web browser developed by Microsoft, based on the Chromium engine.",
        "key_features": [
            "Fast and secure browsing",
            "Built-in privacy features",
            "Integration with Microsoft services",
            "Collections and vertical tabs"
        ],
        "latest_version": "Microsoft Edge (continuous updates)",
        "use_cases": "Web browsing, online shopping, research, productivity"
    }
}

def search_product(query):
    """
    Search for Microsoft products based on query
    Returns relevant products and their information
    """
    query_lower = query.lower()
    results = []
    
    # Direct product match
    for product_name, product_info in MICROSOFT_PRODUCTS_KB.items():
        if product_name.lower() in query_lower:
            results.append((product_name, product_info))
    
    # Keyword search if no direct match
    if not results:
        keywords = {
            "office": ["Microsoft 365"],
            "excel": ["Microsoft 365"],
            "word": ["Microsoft 365"],
            "powerpoint": ["Microsoft 365"],
            "cloud": ["Azure", "Microsoft 365"],
            "database": ["SQL Server"],
            "gaming": ["Xbox"],
            "game": ["Xbox"],
            "browser": ["Edge"],
            "collaboration": ["Teams", "Microsoft 365"],
            "meeting": ["Teams"],
            "analytics": ["Power BI"],
            "visualization": ["Power BI"],
            "crm": ["Dynamics 365"],
            "erp": ["Dynamics 365"],
            "development": ["Visual Studio"],
            "ide": ["Visual Studio"],
            "operating system": ["Windows"],
            "os": ["Windows"]
        }
        
        for keyword, products in keywords.items():
            if keyword in query_lower:
                for product in products:
                    if (product, MICROSOFT_PRODUCTS_KB[product]) not in results:
                        results.append((product, MICROSOFT_PRODUCTS_KB[product]))
    
    return results

def get_product_info(product_name):
    """
    Get detailed information about a specific Microsoft product
    """
    return MICROSOFT_PRODUCTS_KB.get(product_name, None)

def list_all_products():
    """
    List all Microsoft products in the knowledge base
    """
    return list(MICROSOFT_PRODUCTS_KB.keys())
