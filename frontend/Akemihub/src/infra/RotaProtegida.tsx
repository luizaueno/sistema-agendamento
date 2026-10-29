import { Navigate, Outlet } from 'react-router-dom'

export const RotaProtegida = () => {
  const token = localStorage.getItem('token')

  
  if (!token) {
    return <Navigate to="/login" replace />
  }

  return <Outlet />
}
