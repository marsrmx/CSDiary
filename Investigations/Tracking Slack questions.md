# Tracking Slack questions

## Context and Problem Statement

There is a lot of questions coming from Slack channels and there is no way of knowing who answer the questions, amount of effort for it and type of question.

## Proposal

### Ideas

#### @tracker

💡Aplicación de Slack que pueda hacer el tracking de las preguntas y que sea mediante la respuesta del equipo.

`@tracker question resolved`

💡La aplicación debería guardar la pregunta, el hilo, links asociados y quién marcó la pregunta como resuelta.

💡Se podría agregar quién resolvió la pregunta con un parámetro extra.

`@tracker question resolved by x`

💡Al tener una base de datos podrías empezar a ver las preguntas que se repiten cuánto tiempo pasó entre que se escribió en el canal y se marcó como resuelta o incluso notificar a quién esta _oncall_ que la pregunta está sin contestar.

🤔 Cómo diferencias entre una pregunta y un service request o una notificación de qué agregaron un ticket. _Tecnicamente cualquier cosa que salga en el canal de Slack debería ser atendida entonces, tal vez cambiar a `@tracker request resolved.` O precisamente, el usuario puede colocar el tipo de mensaje que fue._

💡Tipos de mensajes posibles:

- question
- request
- notification
- other (?)

[API Slack](https://api.slack.com/start)

#### Qué necesitaríamos

API nos diera acceso a los hilos cuándo se llama la aplicación, los usuarios participantes, el mensaje padre, la fecha y hora, los links y ya.

Un backend que pudiera hacer el tracking de todo lo que esta pasando en una organización.

🤔 Esta es una buena idea, no existirá algo así ya?

🤔 Me preocupa la seguridad de la información, es importante que ellos tengan acceso a esta información y todo sea super transparente.

 

