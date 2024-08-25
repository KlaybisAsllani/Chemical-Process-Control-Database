import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ReactorList = () => {
    const [reactors, setReactors] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/reactors/')
            .then(response => {
                setReactors(response.data);
            })
            .catch(error => {
                console.error("There was an error fetching the reactors!", error);
            });
    }, []);

    return (
        <div>
            <h1>Chemical Engineering Reactors</h1>
            <ul>
                {reactors.map(reactor => (
                    <li key={reactor.id}>
                        <h2>{reactor.name}</h2>
                        <p><strong>Type:</strong> {reactor.reactor_type}</p>
                        <p><strong>Description:</strong> {reactor.description}</p>
                        <p><strong>Benefits:</strong> {reactor.benefits}</p>
                        <p><strong>Uses:</strong> {reactor.uses}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ReactorList;