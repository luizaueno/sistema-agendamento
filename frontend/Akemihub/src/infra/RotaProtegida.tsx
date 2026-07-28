import { Navigate, Outlet } from 'react-router-dom'

export const RotaProtegida = () => {
  const token = localStorage.getItem('token')

  // CORREÇÃO: Redirecionar direto para o endereço de login público
  if (!token) {
    return <Navigate to="/login" replace />
  }

  return <Outlet />
}
