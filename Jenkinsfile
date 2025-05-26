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
                    sudo apt update && sudo apt install -y python3 python3-pip
                    pip3 install -r requirements.txt
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
