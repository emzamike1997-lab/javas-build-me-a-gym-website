```javascript
import React from 'react';
import './Header.css';

function Header({ handlePageChange }) {
    return (
        <header className="header">
            <nav className="nav">
                <ul className="nav-list">
                    <li className="nav-item">
                        <button className="nav-link" onClick={() => handlePageChange('home')}>
                            Home
                        </button>
                    </li>
                    <li className="nav-item">
                        <button className="nav-link" onClick={() => handlePageChange('about')}>
                            About
                        </button>
                    </li>
                    <li className="nav-item">
                        <button className="nav-link" onClick={() => handlePageChange('services')}>
                            Services
                        </button>
                    </li>
                    <li className="nav-item">
                        <button className="nav-link" onClick={() => handlePageChange('contact')}>
                            Contact
                        </button>
                    </li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;
```

###