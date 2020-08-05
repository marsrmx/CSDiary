# React

## Controlled vs Uncontrolled form inputs

Controlled - https://reactjs.org/docs/forms.html#controlled-components

Uncontrolled - https://reactjs.org/docs/uncontrolled-components.html

How to decide? - https://goshakkk.name/controlled-vs-uncontrolled-inputs-react/

## Prop Drilling

https://kentcdodds.com/blog/prop-drilling

https://kentcdodds.com/blog/when-to-break-up-a-component-into-multiple-components

## REDUX

Presentational components care about how things look and containers about how thinks works and interact with data. Containers are usually parent component for a presentational component.

### Containers

Container are **components** that are aware of the application state. Read the state subscribing into the Redux state and change this data using dispatch Redux actions.

Usually this types of components don't include any type of `HTML` inside besides a `<div>` that provided the data for the child *presentational component*. 

### Presentational Components

Part of an application to display static data. It reads the data directly from the *props* and change it invoking callbacks from props.

[Medium saving my ass](https://medium.com/@yassimortensen/container-vs-presentational-components-in-react-8eea956e1cea)

[Another cool Medium article talking about this](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0)

### Testing REDUX

#### Containers

[Medium tutorial](https://medium.com/better-programming/how-to-test-your-react-container-components-fd71071cc3e0)

Haven't implement it yet, but I'll write about it when I do.









