pipeline {
    agent any

    environment {
        STAGE = "staging"
    }

    stages {
        stage('Deploy to Staging') {
            steps {
                echo "Deploying to ${env.STAGE} environment..."
                // Simulate deployment
                sh 'echo "Deployed!"'
            }
        }

        stage('Run Integration Tests') {
            steps {
                sh '''
                    apt install python3.12-venv
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    python test_integration.py
                   
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline completed."
        }
    }
}
