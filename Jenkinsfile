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
                    python3 -m venv venv
                    venv/bin/activate
                    pip install -r requirements.txt
                    python3 test_integration.py
                   
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
