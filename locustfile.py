from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # Define el tiempo de espera entre las tareas de cada usuario simulado
    wait_time = between(1, 5)  # Los usuarios esperan entre 1 y 5 segundos antes de realizar la siguiente tarea
    
    @task
    def visit_home(self):
        """Carga la página principal."""
        self.client.get("/", verify=True)  # Asegúrate de que la verificación SSL esté activada para pruebas de producción

    # Si deseas añadir más tareas para simular interacciones diferentes, simplemente define más métodos con el decorador @task
    # Por ejemplo, para visitar otra página podrías añadir:
    # @task
    # def visit_other_page(self):
    #     self.client.get("/otra-pagina/")
