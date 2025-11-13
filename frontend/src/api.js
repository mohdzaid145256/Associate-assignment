import axios from 'axios';

const API_ROOT = process.env.REACT_APP_API_URL || ''; // if empty, CRA proxy will be used
const api = axios.create({
  baseURL: API_ROOT,
  timeout: 8000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Global response error handler - convert network errors to friendly messages
api.interceptors.response.use(
  (resp) => resp,
  (error) => {
    if (!error.response) {
      // network/CORS or server unreachable
      return Promise.reject(new Error('Network error: backend unreachable (check server)'));
    }
    // propagate server error with message if available
    const msg = error.response?.data?.error || error.response?.statusText || 'Server error';
    return Promise.reject(new Error(msg));
  }
);

export default api;
