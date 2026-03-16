```javascript
import React, { useState, useEffect } from 'react';
import './App.css';
import Header from './components/Header';
import Home from './components/Home';
import About from './components/About';
import Services from './components/Services';
import Contact from './components/Contact';
import Footer from './components/Footer';

function App() {
    const [currentPage, setCurrentPage] = useState('home');

    const handlePageChange = (page) => {
        setCurrentPage(page);
    };

    return (
        <div className="App">
            <Header handlePageChange={handlePageChange} />
            {currentPage === 'home' && <Home />}
            {currentPage === 'about' && <About />}
            {currentPage === 'services' && <Services />}
            {currentPage === 'contact' && <Contact />}
            <Footer />
        </div>
    );
}

export default App;
```

###