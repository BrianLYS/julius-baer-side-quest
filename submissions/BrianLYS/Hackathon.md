# 🏦 Application Modernization Challenge - Hacker Instructions

<div align="center">

## 📱 **Quick Access QR Code**
**Scan to access the challenge repository**

![Challenge Repository QR Code](image.png)

*Scan with your phone to quickly access the GitHub repository*

</div>

---

## 📋 **Challenge Overview**

**Time Limit**: 1.5 hours ⏰  
**Core Task**: Modernize banking client code to integrate with our REST API  
**Supported Languages**: Java, Python, or JavaScript only  
**Goal**: Demonstrate code modernization skills, apply best practices, and upgrade legacy implementations to current standards

---

## 🚀 **Getting Started**

### **Step 1: Run the Mock Banking Server**

#### Using Docker
**Start the server**:
```bash
docker run -d -p 8123:8123 singhacksbjb/sidequest-server:latest
```

#### Using Java
**📚 Need Java installed?** See our comprehensive setup guide: **[SETUP.md](SETUP.md)**

**Quick Java Check:**
```bash
java -version
# Should show Java 17 or higher
```

If you don't have Java 17+, follow the setup guide for installation instructions for your platform.


1. **Navigate to server folder**: `cd server`
2. **The JAR file is located here**: `core-banking-api.jar`
3. **Start the server**:
   ```bash
   java -jar core-banking-api.jar
   ```
   - Server runs on: `http://localhost:8123`
   - Alternative port: `java -Dserver.port=8080 -jar core-banking-api.jar`

4. **Verify server is running**:
   ```bash
   curl http://localhost:8123/accounts/validate/ACC1000
   ```

### **Step 2: Explore the API**

- **Swagger UI**: http://localhost:8123/swagger-ui.html
- **API Documentation**: http://localhost:8123/v3/api-docs
- **Quick Test**: Use the provided **[demo_curls_no_jq.sh](demo_curls_no_jq.sh)** script

**🚀 Run the demo script:**
```bash
# Make it executable and run
chmod +x demo_curls_no_jq.sh
./demo_curls_no_jq.sh
```

This script demonstrates all API endpoints with authentication, transfers, and validation examples.

---

## 🎯 **Core Requirements (Minimum to Pass)**

### **Primary Task: Legacy Code Modernization**
Your mission is to:
1. **Analyze the provided legacy code** examples (see below)
2. **Modernize and refactor** using current best practices
3. **Implement proper REST API integration** for the `/transfer` endpoint
4. **Apply modern coding standards** and design patterns

**Minimum Transfer Request:**
```json
{
  "fromAccount": "ACC1000",
  "toAccount": "ACC1001", 
  "amount": 100.00
}
```

**Example Success Response:**
```json
{
  "transactionId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "status": "SUCCESS",
  "message": "Transfer completed successfully",
  "fromAccount": "ACC1000",
  "toAccount": "ACC1001",
  "amount": 100.00
}
```

---

## 🌟 **Modernization Bonus Points System (Extra Credit)**

### **🥉 Bronze Level - Basic Modernization**

#### **1. Language Modernization (🌟 Standard Bonus)**
- **Python**: Upgrade from 2.7 to 3.x syntax, use modern libraries (requests, asyncio, etc.)
- **JavaScript**: Convert ES5 to ES6+, use modern APIs (fetch, async/await, modules)
- **Java**: Upgrade from Java 6 to 11+, use modern features (HTTP Client, var keyword, streams)

#### **2. HTTP Client Modernization (🌟 Standard Bonus)**
- Replace legacy HTTP libraries with modern alternatives
- Implement proper async/await patterns where applicable
- Add connection pooling and timeout configuration
- Use structured JSON handling instead of string concatenation

#### **3. Error Handling & Logging (🌟 Standard Bonus)**
- Replace print statements with proper logging frameworks
- Implement structured exception handling
- Add meaningful error messages and user feedback
- Include proper HTTP status code handling

### **🥈 Silver Level - Advanced Modernization**

#### **4. Security & Authentication (🏆 Maximum Bonus)**
- Implement JWT authentication with proper token management
- Add input validation and sanitization
- Use secure configuration management
- Implement proper credential handling

#### **5. Code Architecture & Design Patterns (🏆 Maximum Bonus)**
- Apply SOLID principles and clean code practices
- Implement dependency injection where appropriate
- Use modern design patterns (Builder, Factory, etc.)
- Separate concerns with proper layering

#### **6. Modern Development Practices (🏆 Maximum Bonus)**
- Add comprehensive unit and integration tests
- Implement proper configuration management
- Use modern build tools and dependency management
- Add code quality tools (linting, formatting)

### **🥇 Gold Level - Professional Standards**

#### **7. DevOps & Deployment (🏆🏆 Premium Bonus)**
- Add containerization (Docker)
- Implement CI/CD pipeline concepts
- Add health checks and monitoring
- Use environment-based configuration

#### **8. User Experience & Interface (🏆🏆 Premium Bonus)**
- Create modern CLI with proper argument parsing
- Build responsive web interface with modern frameworks
- Add interactive features and real-time updates
- Implement proper user feedback and validation

#### **9. Performance & Scalability (🏆🏆 Premium Bonus)**
- Implement connection pooling and caching
- Add retry logic with exponential backoff
- Use async programming patterns effectively
- Add performance monitoring and metrics

---

## 💡 **Maximizing Productivity with AI for Modernization**

### **Recommended AI Usage for Legacy Code Modernization**
1. **Code Refactoring**: Ask AI to modernize legacy code patterns
2. **Best Practices**: Get recommendations for current language standards
3. **Library Migration**: Find modern alternatives to deprecated libraries
4. **Testing**: Generate unit tests for refactored code
5. **Documentation**: Create migration guides and code comments

### **AI Prompts Examples for Modernization**
```
"Modernize this Python 2.7 code to Python 3.x with best practices"
"Convert this ES5 JavaScript to modern ES6+ with async/await"
"Upgrade this Java 6 code to Java 11+ using modern HTTP client"
"Add proper error handling and logging to this legacy code"
"Generate unit tests for this modernized banking client"
"Create a modern CLI interface replacing this legacy implementation"
```

---

## 📊 **Modernization Scoring Rubric**

| Category | Points | Description |
|----------|--------|-------------|
| **Core Modernization** | 40 pts | Successfully modernized legacy code to work with API |
| **Code Quality** | 20 pts | Clean, modern, well-organized code |
| **Language Modernization** | +10 pts | Proper upgrade to current language standards |
| **HTTP Client Modernization** | +10 pts | Modern HTTP libraries and patterns |
| **Error Handling & Logging** | +10 pts | Professional error management and logging |
| **Architecture & Design** | +15 pts | Modern design patterns and best practices |
| **Testing & Documentation** | +10 pts | Unit tests, README, migration notes |
| **Innovation** | +5 pts | Creative modernization solutions |

**Total Possible**: 120 points (60 base + 60 modernization bonus)

---

## 🏗️ **Legacy Code Examples to Modernize**

### **Example 1: Python 2.7 Legacy Code (Needs Modernization)**
```python
# Legacy Python 2.7 code - MODERNIZE THIS!
import urllib2
import json

def transfer_money(from_acc, to_acc, amount):
    # Old-style string formatting
    url = "http://localhost:8123/transfer"
    
    # Manual JSON encoding
    data = '{"fromAccount":"' + from_acc + '","toAccount":"' + to_acc + '","amount":' + str(amount) + '}'
    
    # Old urllib2 approach
    req = urllib2.Request(url, data)
    req.add_header('Content-Type', 'application/json')
    
    try:
        response = urllib2.urlopen(req)
        result = response.read()
        print "Transfer result: " + result
        return result
    except urllib2.HTTPError, e:
        print "Error: " + str(e.code)
        return None

# Usage - old style
if __name__ == "__main__":
    transfer_money("ACC1000", "ACC1001", 100.00)
```

**🎯 Modernization Tasks:**
- Upgrade to Python 3.x syntax
- Use modern `requests` library
- Add proper error handling and logging
- Implement configuration management
- Add type hints and documentation
- Use f-strings and modern formatting

### **Example 2: Legacy JavaScript (ES5, Needs Modernization)**
```javascript
// Legacy ES5 JavaScript - MODERNIZE THIS!
function transferMoney(fromAccount, toAccount, amount) {
    // Old XMLHttpRequest approach
    var xhr = new XMLHttpRequest();
    var url = "http://localhost:8123/transfer";
    
    // Manual JSON string building
    var data = '{"fromAccount":"' + fromAccount + '","toAccount":"' + toAccount + '","amount":' + amount + '}';
    
    xhr.open("POST", url, false); // Synchronous - BAD!
    xhr.setRequestHeader("Content-Type", "application/json");
    
    try {
        xhr.send(data);
        if (xhr.status == 200) {
            var result = JSON.parse(xhr.responseText);
            console.log("Transfer successful: " + result.transactionId);
            return result;
        } else {
            console.log("Error: " + xhr.status);
            return null;
        }
    } catch (e) {
        console.log("Request failed: " + e.message);
        return null;
    }
}

// Usage - old style
transferMoney("ACC1000", "ACC1001", 100.00);
```

**🎯 Modernization Tasks:**
- Convert to ES6+ syntax (const/let, arrow functions)
- Use modern `fetch` API or `axios`
- Implement async/await pattern
- Add proper error handling with try/catch
- Use template literals for strings
- Add input validation and sanitization
- Implement proper logging and debugging

### **Example 3: Java 6 Legacy Code (Needs Modernization)**
```java
// Legacy Java 6 code - MODERNIZE THIS!
import java.io.*;
import java.net.*;

public class BankingClient {
    private String baseUrl = "http://localhost:8123";
    
    public String transferFunds(String fromAccount, String toAccount, double amount) {
        try {
            // Old URL and HttpURLConnection approach
            URL url = new URL(baseUrl + "/transfer");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            
            // Manual JSON string building
            String jsonData = "{\"fromAccount\":\"" + fromAccount + 
                             "\",\"toAccount\":\"" + toAccount + 
                             "\",\"amount\":" + amount + "}";
            
            // Old-style connection setup
            conn.setDoOutput(true);
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
            
            // Manual stream handling
            OutputStream os = conn.getOutputStream();
            os.write(jsonData.getBytes());
            os.flush();
            os.close();
            
            // Manual response reading
            BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String line;
            StringBuffer response = new StringBuffer();
            while ((line = br.readLine()) != null) {
                response.append(line);
            }
            br.close();
            
            System.out.println("Response: " + response.toString());
            return response.toString();
            
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
            return null;
        }
    }
    
    // Usage - old style
    public static void main(String[] args) {
        BankingClient client = new BankingClient();
        client.transferFunds("ACC1000", "ACC1001", 100.00);
    }
}
```

**🎯 Modernization Tasks:**
- Upgrade to Java 11+ features (var, HTTP Client API)
- Use modern JSON libraries (Jackson, Gson)
- Implement proper exception handling
- Add logging framework (SLF4J, Logback)
- Use dependency injection and configuration
- Add unit tests with JUnit 5
- Implement builder patterns and immutable objects
- Use modern HTTP client libraries

---

## 📁 **Code Submission**

### **🎯 Primary Method: GitHub Pull Request (Recommended)**

#### **Step 1: Access the Challenge Repository**
1. **Repository URL**: `https://github.com/SingHacks-2025/julius-baer-side-quest` (provided by instructor)
2. **Fork the repository** to your GitHub account
3. **Clone your fork** locally:
   ```bash
   git clone https://github.com/SingHacks-2025/julius-baer-side-quest.git
   cd core-banking-hackathon-submissions
   ```

#### **Step 2: Create Your Submission Folder**
1. **Create a folder** in `/submissions/` named after your GitHub username:
   ```bash
   mkdir submissions/your-github-username
   cd submissions/your-github-username
   ```
   
2. **Example structure**:
   ```
   submissions/
   ├── mark-h/
   │   ├── banking_client.py
   │   ├── README.md
   │   └── requirements.txt
   ├── john-doe/
   │   ├── BankingClient.java
   │   ├── README.md
   │   └── pom.xml
   └── your-github-username/
       ├── [your solution files]
       └── README.md
   ```

#### **Step 3: Submit via Pull Request**
1. **Add and commit** your files:
   ```bash
   git add submissions/your-github-username/
   git commit -m "Add banking client solution by [your-name]"
   ```

2. **Push to your fork**:
   ```bash
   git push origin main
   ```

3. **Create Pull Request**:
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - **Title**: `Banking Client Solution - [Your Name]`
   - **Description**: Include language used, key features implemented, and how to run

#### **Step 4: Pull Request Template**
Use this template in your PR description:

```
## Hacker Submission

**Name**: [Your Full Name]
**GitHub Username**: [your-username]
**Email**: [your-email@example.com]
**LinkedIn**: [https://linkedin.com/in/your-profile]
**Programming Language**: [Java/Python/JavaScript]
**Time Spent**: [e.g., 1.5 hours]

### Features Implemented
- [x] Core transfer functionality
- [x] JWT authentication (if implemented)
- [x] Error handling (if implemented)
- [ ] Additional features...

### How to Run
# Your setup and run commands here
# Example:
# python banking_client.py
# or
# java -cp . BankingClient

### Bonus Features
- Brief description of any bonus features implemented

### Questions/Notes
- Any questions or notes for the mentor
```

---

## 📦 **Alternative Submission Method**

### **Option 2: ZIP Submission (Fallback)**
If GitHub is not accessible or you prefer this method:

1. **Create a project folder**:
   ```bash
   mkdir banking-client-[your-github-username]
   cd banking-client-[your-github-username]
   ```

2. **Add your solution files**:
   - Source code files
   - README.md with setup instructions
   - Dependencies file (requirements.txt, package.json, etc.)
   - Any test files

3. **Create the ZIP file**:
   ```bash
   # Navigate back to parent directory
   cd ..
   # Create ZIP file
   zip -r banking-client-[your-github-username].zip banking-client-[your-github-username]/
   ```
   # send it to jbsidequest@proton.me


4. **Submit the ZIP file** as instructed by your mentor

### **📋 Required Files (All Methods)**
- **Source Code**: Your client implementation
- **README.md**: Setup instructions, usage examples, features implemented
- **Dependencies**: `requirements.txt`, `package.json`, `pom.xml`, etc. (if applicable)
- **Tests**: Test files (bonus points)
- **Documentation**: Any additional docs or screenshots

### **⚠️ Important Submission Notes**
- **Deadline**: Submit within 1.5 hours of starting
- **Folder Naming**: Use your GitHub username exactly (case-sensitive)
- **No Merge Conflicts**: Pull latest changes before pushing if using folder method
- **File Size**: Keep submissions under 10MB (no large binaries)
- **Public Repository**: The challenge repo is public - your solution will be visible to others after submission

---

## 🎯 **Success Tips**

### **Time Management (1.5 hours)**
- **20 min**: Setup, explore API, plan approach
- **50 min**: Implement core transfer functionality
- **20 min**: Add one bonus feature (auth or validation)
- **10 min**: Documentation and cleanup

### **Prioritization**
1. **First**: Get basic transfer working
2. **Second**: Add JWT authentication
3. **Third**: Add error handling
4. **Fourth**: Choose one advanced feature
5. **Last**: Polish documentation

### **Common Pitfalls to Avoid**
- Don't spend too much time on UI if you're not comfortable with it
- Don't try to implement all bonus features - pick 2-3 and do them well
- Don't forget to test your client against the actual server
- Don't skip documentation - it's easy bonus points

---

## 🏦 **API Quick Reference**

### **Core Endpoints**
| Method | Endpoint | Purpose | Auth Required |
|--------|----------|---------|---------------|
| `POST` | `/authToken` | Get JWT token | No |
| `POST` | `/transfer` | Transfer funds | No (bonus if yes) |
| `GET` | `/accounts` | List accounts | No (bonus if yes) |
| `GET` | `/accounts/validate/{id}` | Validate account | No (bonus if yes) |

### **Bonus Endpoints**
| Method | Endpoint | Purpose | Auth Required |
|--------|----------|---------|---------------|
| `POST` | `/auth/validate` | Validate JWT | Yes |
| `GET` | `/transactions/history` | Transaction history | Yes |
| `GET` | `/accounts/balance/{id}` | Account balance | No (bonus if yes) |

### **Account Ranges**
- **Valid**: ACC1000-ACC1099 (can send/receive funds)
- **Invalid**: ACC2000-ACC2049 (transfers will fail)
- **Non-existent**: All others (transfers will fail)

---

## 🎉 **Final Notes**

- **Focus on meaningful modernization** over cosmetic changes
- **Use AI tools** to accelerate the refactoring process
- **Test frequently** against the live server during modernization
- **Document your modernization decisions** in the README
- **Show before/after comparisons** to highlight improvements!

**Remember**: The goal is to demonstrate your ability to modernize legacy code using current best practices. A well-refactored, working solution with clear improvements beats a complex rewrite that doesn't work!

Good luck! 🚀

---

*Questions? Ask your mentor or check the Swagger UI at http://localhost:8123/swagger-ui.html*
