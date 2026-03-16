```javascript
import React, { useState } from 'react';
import './Contact.css';

function Contact() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');
    const [error, setError] = useState(null);

    const handleSubmit = (event) => {
        event.preventDefault();
        if (!name || !email || !message) {
            setError('Please fill out all fields');
            return;
        }
        // Send email using API or email service
        console.log('Form submitted:', { name, email, message });
        setError(null);
    };

    return (
        <section className="contact">
            <h1 className="contact-title">Get in Touch</h1>
            <form className="contact-form" onSubmit={handleSubmit}>
                <label className="contact-label" htmlFor="name">
                    Name:
                </label>
                <input
                    className="contact-input"
                    type="text"
                    id="name"
                    value={name}
                    onChange={(event) => setName(event.target.value)}
                />
                <label className="contact-label" htmlFor="email">
                    Email:
                </label>
                <input
                    className="contact-input"
                    type="email"
                    id="email"
                    value={email}
                    onChange={(event) => setEmail(event.target.value)}
                />
                <label className="contact-label" htmlFor="message">
                    Message:
                </label>
                <textarea
                    className="contact-textarea"
                    id="message"
                    value={message}
                    onChange={(event) => setMessage(event.target.value)}
                />
                {error && <p className="contact-error">{error}</p>}
                <button className="contact-cta" type="submit">
                    Send
                </button>
            </form>
        </section>
    );
}

export default Contact;
```

###