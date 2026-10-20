pipeline {
    agent any

    /*
     * Assignment 6 – Jenkins Integration with GitHub
     * Declarative Pipeline (Jenkinsfile)
     *
     * Stages:
     *   1. Checkout  – Pull latest code from GitHub
     *   2. Build     – Run the Python application
     *   3. Test      – Execute inline tests inside app.py
     *   4. Archive   – Store build artifacts in Jenkins
     */

    environment {
        APP_NAME    = 'devops-demo'
        BRANCH      = 'main'
    }

    stages {

        stage('Checkout') {
            steps {
                echo "📥 Cloning repository from GitHub (branch: ${env.BRANCH})..."
                git branch: "${env.BRANCH}",
                    url: 'https://github.com/Strix33/devops-assignment.git'
                echo "✅ Repository checked out successfully."
                sh 'ls -la'          // List workspace contents (Linux/Mac)
                // bat 'dir'          // Uncomment on Windows agents
            }
        }

        stage('Build') {
            steps {
                echo "🔨 Building ${env.APP_NAME}..."
                sh 'python --version'
                sh 'python app.py'
            }
        }

        stage('Test') {
            steps {
                echo "🧪 Running test suite..."
                // Try pytest first; fall back to inline tests in app.py
                sh '''
                    if python -m pytest --version > /dev/null 2>&1; then
                        python -m pytest app.py -v --tb=short
                    else
                        echo "pytest not found – running app tests directly"
                        python app.py
                    fi
                '''
            }
        }

        stage('Archive') {
            steps {
                echo "📦 Archiving build artifacts..."
                archiveArtifacts artifacts: '**/*.py, **/*.html, **/README.md',
                                 allowEmptyArchive: true,
                                 fingerprint: true
            }
        }
    }

    post {
        success {
            echo "🎉 Pipeline SUCCEEDED – Build #${env.BUILD_NUMBER} completed."
        }
        failure {
            echo "💥 Pipeline FAILED – Check console output for details."
        }
        always {
            echo "🏁 Pipeline finished. Duration: ${currentBuild.durationString}"
        }
    }
}
