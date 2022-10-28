import styles from '../styles/Home.module.css'
import { useState } from 'react'

export default function Home() {
  const apiUrl = `${process.env.NEXT_PUBLIC_API_URL}` || 'http://localhost:8000'
  const [number, setNumber] = useState(0)
  const [answer, setAnswer] = useState('')
  const onSubmit = (e) => {
    e.preventDefault()
    fetch(`${apiUrl}/api/v1/foobar`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ number }),
    })
      .then((res) => res.json())
      .then((data) => setAnswer(data.result))
  }

  return (
    <div className={styles.container}>
      <main className={styles.main}>
        <h1 className={styles.title}>Welcome to the FooBar service</h1>
        <form onSubmit={onSubmit}>
          <label className={styles.description}>Your number</label>
          <input
            className={styles.input}
            type="text"
            name="number"
            onChange={(e) => setNumber(e.target.value)}
          />
          <button className={styles.button} type="submit">
            Submit
          </button>
        </form>
        <code className={styles.code}>Answer: {answer}</code>
      </main>
    </div>
  )
}
