def generate_sample_data(blueprint_list):
    """
    Generate sample data for each blueprint.
    Each blueprint gets 5 sample entries with realistic data.
    """
    sql = []
    
    # Sample data templates for different types of blueprints
    sample_data = {
        'admin': [
            ("Admin User", "System administrator with full access"),
            ("Content Manager", "Manages website content and updates"),
            ("Support Staff", "Handles user support and inquiries"),
            ("Moderator", "Moderates user content and comments"),
            ("Analyst", "Analyzes system usage and performance")
        ],
        'users': [
            ("John Doe", "Regular user account"),
            ("Jane Smith", "Premium user account"),
            ("Bob Wilson", "New user account"),
            ("Alice Brown", "Verified user account"),
            ("Charlie Davis", "Inactive user account")
        ],
        'reports': [
            ("Monthly Sales", "Summary of monthly sales figures"),
            ("User Activity", "Daily user activity metrics"),
            ("System Health", "System performance and health check"),
            ("Error Logs", "Application error and warning logs"),
            ("Audit Trail", "Security and access audit records")
        ],
        'products': [
            ("Basic Plan", "Entry level subscription plan"),
            ("Premium Plan", "Advanced features subscription"),
            ("Enterprise Plan", "Full feature set for businesses"),
            ("Starter Kit", "Basic product package"),
            ("Professional Kit", "Complete product package")
        ],
        'orders': [
            ("Order #1001", "Pending order from John Doe"),
            ("Order #1002", "Completed order from Jane Smith"),
            ("Order #1003", "Processing order from Bob Wilson"),
            ("Order #1004", "Shipped order from Alice Brown"),
            ("Order #1005", "Delivered order from Charlie Davis")
        ]
    }

    # Generate sample data for each blueprint
    for bp in blueprint_list:
        # Get sample data for this blueprint type, or use a default if not found
        data = sample_data.get(bp, [
            (f"{bp.title()} Item 1", f"Description for {bp} item 1"),
            (f"{bp.title()} Item 2", f"Description for {bp} item 2"),
            (f"{bp.title()} Item 3", f"Description for {bp} item 3"),
            (f"{bp.title()} Item 4", f"Description for {bp} item 4"),
            (f"{bp.title()} Item 5", f"Description for {bp} item 5")
        ])
        
        # Generate INSERT statements
        for name, description in data:
            sql.append(f"INSERT INTO {bp} (name, description) VALUES ('{name}', '{description}');")
    
    return "\n".join(sql) 