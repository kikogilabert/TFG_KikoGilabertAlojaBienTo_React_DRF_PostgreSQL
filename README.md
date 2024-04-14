# 🏢 AlojaBienTo2

## Indice:

1. ¿Que es AlojaBienTo2?
2. Tecnologias implementadas
3. Desarrollo de los modulos

# AlojaBienTo2:  

 AlojaBienTo2 es un proyecto desarrollado y diseñado por [`Kiko Gilabert Mañó`](https://github.com/kikogilabert). Fue creado para cubrir las necesidades del alquiler vacacional de apartamentos. Por una parte, los usuarios tendrán la posibilidad de alquilar y reservar distintos apartamentos en diferentes ubicaciones y fechas. Además, hemos implementado un panel de Administrador que se encarga de gestionar los apartamentos, zonas, ciudades, reservas, usuarios, notificaciones y incidencias. Por último, hemos añadido un login y register para que los usuarios puedan registrarse y loguearse en la aplicación, tanto de manera local como de manera social con Google y Facebook.


# 🔹 Documentación:  

En el enlace [DOCUMENTACIÓN](#) encontrarás la documentación completa del proyecto AlojaBiento2, que incluye análisis y requerimientos detallados, así como los aspectos más importantes de la aplicación. Esta documentación te permitirá comprender en detalle cómo se ha planificado y desarrollado el proyecto, brindando información esencial para su implementación exitosa. Es una fuente valiosa para aquellos interesados en conocer los análisis y requisitos clave, así como los aspectos destacados de la aplicación en el contexto del proyecto AlojaBiento2.

# 🔹 Tecnologías:

<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"
                 alt="React" />
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green"
                alt="Django" />

## 🔸 Backend

- ### [Django Rest FW](https://www.django-rest-framework.org) 

  - Migrations
  - Models
  - Views
  - Serializers
  - Postgresql
    - Relationships
    - Schema
  - Middleware_auth
    - Header
    - Token JWT

## 🔸 Frontend

- ### [React 18](https://es.reactjs.org)

  - Lazy load
  - Guards
  - Service with axios
  - Authentication JWT
  - Context
  - Hooks
  - Custom notifications
  - Librerias:
    - Bootstrap
    - Tailwind
    - FontAwesome
    - Recaptcha v3
    - Firebase

## 🔸 Base de datos:

  - [PostgreSQL](https://www.postgresql.org/)

# 🔹 Desarrollo de los modulos:  

##  📌  Home
  - Es la página principal, a primera vista podemos ver un apartado con las ciudades mas destacadas y un about us que explica nuestra empresa, mas abajo tenemos un apartado de los apartamentos mas destacados.
  ![Foto Home](image.png)

##  🏙  Cities
  - En esta vista podremos ver todas las ciudades disponibles, y al hacer click en una de ellas nos redirigira a todas las zonas con apartamentos disponibles en el momento de dicha ciudad.
  ![Foto Cities](image.png)

##  🏠  Zones
  - En esta vista podremos ver todas las zonas disponibles, y al hacer click en una de ellas nos redirigira a todos los apartamentos disponibles en el momento de dicha zona.
  ![Foto Zones](image.png)

##  📝  Rents/Apartments
  - Es de las vistas mas importantes, en ella podremos ver todos los apartamentos disponibles, filtrar por ciudad, habitaciones y baños.
  ![Foto Filtros](image.png)

  - Ademas podremos ver la información de cada apartamento y reservarlo si esta disponible.

##  🔑 Login/Register
- Son la views que el usuario tendrá la opción de registrarse y loguearse, hemos utilizado modales y formularios de [React-Boostrap](https://react-bootstrap.netlify.app/docs/components/modal/), para que el usuario pueda loguearse de manera sencilla y rápida. Además, hemos añadido la opción de loguearse con Google y Facebook, para que el usuario pueda acceder a la aplicación de manera más rápida y sencilla.

## 👨🏼‍🦱  Profile
-  Encontraremos todos los datos del usuario, podremos ver las resevas realizadas y las notificaciones, tanto vistas como por ver.

## 📩  Notifications
- En header tendremos una opción que se encargará de avisarte de cuándo tienes alguna notificación sobre las reservas y tienes un desplegable en el que visualizar las notificaciones una vez entres.

## 📎 Dashboard Admin
- En la view de Dashboard podremos ver un registro de (Apartments / Zones / Cities / Users) en los cuales el administrador podrá modificar, crear y borrar según le resulte necesario.
