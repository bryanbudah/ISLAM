module.exports = {
  darkMode: 'class', // Enables class-based dark mode
  content: [
    './templates/**/*.html',
    './theme/templates/**/*.html',
    './users/templates/**/*.html',
    './core/templates/**/*.html',
    './content/templates/**/*.html',
    './**/forms.py', // For Tailwind forms plugin
     './static/src/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          light: '#38a169', // Green-600
          DEFAULT: '#2f855a', // Green-700
          dark: '#276749', // Green-800
        },
        secondary: {
          light: '#f6ad55', // Amber-400
          DEFAULT: '#ed8936', // Amber-500
          dark: '#dd6b20', // Amber-600
        },
        islamic: {
          gold: '#d4af37',
          green: '#228B22', // Islamic green
          navy: '#000080', // Islamic navy
        },
      },
      fontFamily: {
        arabic: ['"Amiri"', '"Traditional Arabic"', 'serif'],
        sans: [
          'Inter',
          'system-ui',
          '-apple-system',
          'BlinkMacSystemFont',
          '"Segoe UI"',
          'Roboto',
          '"Helvetica Neue"',
          'Arial',
          '"Noto Sans"',
          'sans-serif',
        ],
        serif: [
          '"Amiri"',
          'Georgia',
          'Cambria',
          '"Times New Roman"',
          'Times',
          'serif',
        ],
      },
      boxShadow: {
        'islamic': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06), 0 0 0 3px rgba(34, 139, 34, 0.5)',
      },
      backgroundImage: {
        'mosque-pattern': "url('../static/images/mosque-pattern-light.png')",
        'mosque-pattern-dark': "url('../static/images/mosque-pattern-dark.png')",
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'), // For beautiful form styling
    require('@tailwindcss/typography'), // For prose content
    require('@tailwindcss/aspect-ratio'), // For media handling
    require('@tailwindcss/line-clamp'), // For text truncation
  ],
  
}