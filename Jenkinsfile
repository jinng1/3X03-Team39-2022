pipeline {
    agent {dockerfile { filename 'Dockerfile.Jenkins' }}

    stages {
		// stage('Build') {
		//     steps {
		// 	    echo 'building'
		//     }
		// }
        stage("Testing"){
            steps{
		        echo "hello world"
            }
        }
        stage("Deploying"){
            steps{
                echo 'deploying'
                sh 'python3 manage.py runserver'
            }
        }
    }
}