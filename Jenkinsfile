pipeline {
    agent any
    stages {
        stage("Testing"){
            agent {
                dockerfile {
                    filename 'Dockerfile.Jenkins'
                }
            }
            steps{
                echo 'testing'
                sh 'pytest tests.py'
            }
        }
        stage('OWASP DependencyCheck') {
			steps {
				dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'Dependency Checker'
			}
		}
    }
    post {
		success {
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		}
	}

}