# homework12
Домашнее задание 12 <br>
Web-страничка принимает логин и пароль и обрабатывает через питон-скрипт. Образ в Docker Hub собирается автоматически по git push. <br>
На виртуальном сервере поднят кластер k8s: <br>
gcloud container clusters create hello-cluster <br>
gcloud container clusters get-credentials hello-cluster <br>
Запуск приложения через yaml-файл: <br>
kubectl apply -f manifest.yml
