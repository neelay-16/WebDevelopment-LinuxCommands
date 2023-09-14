# WebDevelopment-LinuxCommands
Run linux commands using web development

# Preview

https://github.com/neelay-16/WebDevelopment-LinuxCommands/assets/135517502/3b80d6c5-505a-4a7f-ac01-ea1b9e5f3c81

# Description

# [Front End]

This HTML and JavaScript code creates a web page with a simple user interface for running Linux commands on a remote server and displaying the command's output on the webpage. Let's break down the code step by step:

<!DOCTYPE html> and <html lang="en">: These lines define the document type and specify that the language of the document is English.

<head>: This section contains metadata about the web page, such as character encoding, viewport settings, and the page title.

<meta charset="UTF-8">: Sets the character encoding to UTF-8, which is a standard for encoding text on the web.

<meta name="viewport" content="width=device-width, initial-scale=1.0">: Defines the viewport settings, ensuring that the webpage is displayed properly on various devices by scaling it according to the device's width.

<title>Linux Command Output</title>: Sets the title of the webpage to "Linux Command Output."

<style>: This section contains CSS (Cascading Style Sheets) rules for styling the webpage.

It defines the webpage's background, fonts, layout, and styling for various elements like buttons and input fields.
It creates a semi-transparent overlay on the background image for aesthetics.
It styles the container that holds the command input and output fields.
It sets the color and appearance of the heading, labels, input fields, and buttons.
<body>: This section contains the actual content of the webpage.
It starts with a background overlay and a container to center the content on the page.

Inside the container, there's an <h1> element with the title "Linux Command Output."

A label and an input field are provided for users to enter their Linux commands.

A button with the text "Enter" is available for users to submit their commands.

Below the button, there's a <div> with the id "output" that will display the output of the Linux command. The output is displayed inside a <pre> (preformatted text) element.

<script>: This section contains JavaScript code for handling user interactions and making asynchronous requests to a remote server.

The lw() function is defined. When the "Enter" button is clicked, this function is called.

Inside the function, an XMLHttpRequest is created. It's used to send a request to a server and handle the response asynchronously.

The value entered in the input field with the id "in1" is retrieved and stored in the mycmd variable.

The xhr.open() method is used to open a GET request to a specific URL. The URL includes the command provided by the user as a query parameter.

The xhr.send() method sends the GET request to the server.

The xhr.onreadystatechange event handler is used to check the request's state. When the request is complete (readyState == 4), the response from the server is displayed in the "output" <div> by setting the content of the <p> element with the id "p1" to the response text.

Overall, this code creates a web page that allows users to input Linux commands, sends those commands to a remote server, and displays the command output on the webpage when the server responds.


# [Back End]

This Python script appears to be a CGI script that allows you to execute various commands on a server and display the results as an HTML response. Let's break down the code step by step:

1. Shebang and Import Statements:

  ![image](https://github.com/neelay-16/WebDevelopment-LinuxCommands/assets/135517502/fb9fff5f-6860-41f5-8107-aab8362e7a9e)

1. The shebang (#!/usr/bin/python3) specifies the interpreter that should be used to run the script, which is Python 3 in this case.
2. subprocess is imported to run shell commands from within the script.
3. cgi is imported to handle Common Gateway Interface (CGI) input and output.
4. boto3 is imported to interact with AWS services, specifically EC2.


2. Setting HTTP Headers:

![image](https://github.com/neelay-16/WebDevelopment-LinuxCommands/assets/135517502/5384be9a-98ea-4cfe-84dd-18c1e4ad026f)

This sets the HTTP response headers. It specifies that the content type is text/html, indicating that the response will be HTML content.

3. Parsing CGI Input:

  ![image](https://github.com/neelay-16/WebDevelopment-LinuxCommands/assets/135517502/067d4e51-60da-433c-ab19-c8ac39cce215)

This code parses CGI input data. It retrieves the value of the parameter named "c" from the CGI input. This parameter is expected to contain the command to be executed.


4. Command Execution and Output Display:

  ![image](https://github.com/neelay-16/WebDevelopment-LinuxCommands/assets/135517502/b28c3eec-e60e-4fbb-9325-2f26e194fdd1)

The script checks the value of cmd (the command to be executed) and executes different commands based on its content. Here are the supported commands and their actions:
1. docker ps: List running Docker containers and display their details.
2. date: Display the current date and time.
3. cal: Display a calendar.
4. ls: List files and directories in the current directory.
5. pwd: Display the current working directory.
6. docker images: List Docker images and display their details.
7. aws ec2 launch: Launch an AWS EC2 instance using the provided AWS access and secret keys.


5. Default Case

![image](https://github.com/neelay-16/WebDevelopment-LinuxCommands/assets/135517502/0f386f55-2176-48ea-b708-24bef3d272df)

If the command doesnt match any of the predefined commands, the script assumes it's a custom shell command and executes it using subprocess.getoutput(). The output is then printed in the HTML response.

  







