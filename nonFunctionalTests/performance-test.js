import http from 'k6/http';
import { sleep, check } from 'k6';

export default function () {

  const res = http.get('http://127.0.0.1:5001/people/12/');

  sleep(1);

  const checkRes = check(res, {
    'status is 200': (r) => r.status === 200,
    "Name is correct": (r) => r.json()[0]["name"] === "Obi Wan Kenobi"
  });
}