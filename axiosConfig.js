const baseUrl = 'http://localhost'

const instance_api = axios.create({
    baseURL: `${baseUrl}:5000/ong`,
    headers: {
        'Content-Type': 'application/json',
    },
});

function getAxiosInstance() {
    return instance_api;
}