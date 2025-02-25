import os
import subprocess

# Set environment variables
os.environ['JAVA_HOME'] = 'C:/Program Files/Java/jdk-11'

# Define variables
classpath = 'C:/RamiFakhry/GraphQL/client/SiliconCedarsMyGraphQL-0.0.1-SNAPSHOT.jar'
 
java_exec = f"{os.environ['JAVA_HOME']}/bin/java"

# Run the application
try:
    subprocess.run(
        [java_exec, '-Dspring.profiles.active=dev', '-jar', classpath],
        check=True
    )
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")


# netstat -ano | findstr :8080
# taskkill /PID 4504 /F
# curl http://0.0.0.0:4000/graphqlcsv/graphql  
 
