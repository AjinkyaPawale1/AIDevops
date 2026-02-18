"""
Microsoft Products Chat Application
A simple chat interface to answer questions about Microsoft products
"""

from knowledge_base import MICROSOFT_PRODUCTS_KB, search_product, get_product_info, list_all_products


class MicrosoftProductsChat:
    """Chat application for Microsoft products information"""
    
    def __init__(self):
        self.running = True
        
    def display_welcome(self):
        """Display welcome message"""
        print("=" * 70)
        print("Microsoft Products Chat Assistant".center(70))
        print("=" * 70)
        print("\nWelcome! I can help you learn about Microsoft products.")
        print("\nAvailable commands:")
        print("  - Ask about any Microsoft product (e.g., 'Tell me about Azure')")
        print("  - 'list' - Show all available products")
        print("  - 'help' - Show this help message")
        print("  - 'quit' or 'exit' - Exit the application")
        print("\n" + "=" * 70 + "\n")
    
    def display_help(self):
        """Display help message"""
        print("\nHow to use this chat:")
        print("  - Ask questions about Microsoft products naturally")
        print("  - Examples:")
        print("    * 'What is Azure?'")
        print("    * 'Tell me about Windows'")
        print("    * 'What products help with collaboration?'")
        print("    * 'Show me database products'")
        print("\nAvailable products:")
        products = list_all_products()
        for i, product in enumerate(products, 1):
            print(f"  {i}. {product}")
        print()
    
    def display_product_info(self, product_name, product_info):
        """Display detailed information about a product"""
        print(f"\n{'=' * 70}")
        print(f"{product_name}".center(70))
        print(f"{'=' * 70}")
        print(f"\n{product_info['description']}\n")
        print(f"Latest Version: {product_info['latest_version']}")
        print(f"\nKey Features:")
        for feature in product_info['key_features']:
            print(f"  • {feature}")
        print(f"\nUse Cases: {product_info['use_cases']}")
        print(f"{'=' * 70}\n")
    
    def process_query(self, query):
        """Process user query and provide appropriate response"""
        query_lower = query.lower().strip()
        
        # Handle commands
        if query_lower in ['quit', 'exit', 'q']:
            print("\nThank you for using Microsoft Products Chat Assistant. Goodbye!")
            self.running = False
            return
        
        if query_lower in ['help', 'h', '?']:
            self.display_help()
            return
        
        if query_lower == 'list':
            print("\nAvailable Microsoft Products:")
            products = list_all_products()
            for i, product in enumerate(products, 1):
                print(f"  {i}. {product}")
            print(f"\nTotal: {len(products)} products")
            print("Ask me about any of these products!\n")
            return
        
        # Search for products
        results = search_product(query)
        
        if not results:
            print("\nI couldn't find specific information about that.")
            print("Try asking about one of these products:")
            products = list_all_products()
            for product in products[:5]:
                print(f"  • {product}")
            print("\nOr type 'list' to see all available products.")
            print()
            return
        
        # Display results
        if len(results) == 1:
            product_name, product_info = results[0]
            self.display_product_info(product_name, product_info)
        else:
            print(f"\nI found {len(results)} relevant Microsoft products:\n")
            for i, (product_name, product_info) in enumerate(results, 1):
                print(f"{i}. {product_name}")
                print(f"   {product_info['description'][:100]}...")
                print()
            print("Ask about a specific product for more details!\n")
    
    def run(self):
        """Main application loop"""
        self.display_welcome()
        
        while self.running:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                self.process_query(user_input)
                
            except KeyboardInterrupt:
                print("\n\nThank you for using Microsoft Products Chat Assistant. Goodbye!")
                break
            except EOFError:
                print("\n\nThank you for using Microsoft Products Chat Assistant. Goodbye!")
                break
            except Exception as e:
                print(f"\nAn error occurred: {e}")
                print("Please try again.\n")


def main():
    """Main entry point"""
    chat = MicrosoftProductsChat()
    chat.run()


if __name__ == "__main__":
    main()
