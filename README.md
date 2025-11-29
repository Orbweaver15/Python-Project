# Banking Management System

A comprehensive console-based banking application with multi-level user authentication and transaction management.

## 🏦 Features
- **Multi-level Access Control**: Super Admin, Admin, and Customer roles
- **Account Management**: Create, approve, and manage bank accounts
- **Transaction Processing**: Withdrawals, deposits, and balance management
- **Automated Reporting**: Generate transaction reports with date filtering
- **Secure Authentication**: Role-based login system with password protection
- **Data Persistence**: File-based storage for accounts and transactions

## 👥 User Roles
- **Super Admin**: Full system control + Admin account creation
- **Admin**: Customer approval, detail modification, reporting
- **Customer**: Banking operations (withdraw, deposit, password change)

## 🛠 Tech Stack
- **Language**: Python 3
- **Storage**: Text-based file system
- **Libraries**: datetime, random, string, re

## 🚀 Quick Start
1. Run: `python banking_system.py`
2. Follow on-screen instructions
3. Data files are automatically created in `/data` directory
## 📊 Account Types
- **Savings**: Minimum balance 100 RM
- **Current**: Minimum balance 500 RM
