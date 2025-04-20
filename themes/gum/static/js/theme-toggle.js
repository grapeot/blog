(function() {
    const toggleButton = document.getElementById('theme-toggle');
    const lightCss = document.querySelector('link[href*="pygment.css"]:not([href*="dark"])'); // Find the light pygments CSS
    const darkCss = document.getElementById('pygment-dark-link');
    const htmlElement = document.documentElement;
    const moonIcon = '🌙';
    const sunIcon = '☀️';

    // Function to apply the theme
    function applyTheme(theme) {
        if (theme === 'dark') {
            htmlElement.setAttribute('data-theme', 'dark');
            if (darkCss) darkCss.disabled = false;
            if (lightCss && darkCss) lightCss.media = 'not all'; // Disable light theme by setting media query to something that doesn't match
            if (toggleButton) toggleButton.textContent = sunIcon; // Show sun icon when in dark mode
        } else {
            htmlElement.removeAttribute('data-theme');
            if (darkCss) darkCss.disabled = true;
            if (lightCss) lightCss.media = 'all'; // Re-enable light theme
            if (toggleButton) toggleButton.textContent = moonIcon; // Show moon icon when in light mode
        }
        // Store the preference
        try {
            localStorage.setItem('theme', theme);
        } catch (e) {
            console.warn('LocalStorage is not available for saving theme preference.');
        }
    }

    // Function to determine the initial theme
    function getInitialTheme() {
        let storedTheme = null;
        try {
            storedTheme = localStorage.getItem('theme');
        } catch (e) { /* LocalStorage not available */ }

        if (storedTheme && (storedTheme === 'dark' || storedTheme === 'light')) {
            return storedTheme;
        } else {
            // Check system preference if no stored theme
            if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
                return 'dark';
            }
        }
        return 'light'; // Default to light
    }

    // Add event listener to the button
    if (toggleButton) {
        toggleButton.addEventListener('click', () => {
            const currentTheme = htmlElement.hasAttribute('data-theme') ? 'dark' : 'light';
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            applyTheme(newTheme);
        });
    }

    // Apply the initial theme on load
    const initialTheme = getInitialTheme();
    applyTheme(initialTheme);

    // Optional: Add listener for changes in system preference
    if (window.matchMedia) {
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', event => {
            // Only change if the user hasn't manually selected a theme (or if they selected 'auto')
            let storedTheme = null;
            try {
                 storedTheme = localStorage.getItem('theme');
            } catch (e) { /* LocalStorage not available */ }

            // We assume null or 'auto' means follow system. If 'light' or 'dark' is stored, user preference overrides.
            if (!storedTheme || storedTheme === 'auto') {
                const newColorScheme = event.matches ? 'dark' : 'light';
                applyTheme(newColorScheme);
            }
        });
    }

})(); 