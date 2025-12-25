"use client"

import type React from "react"
import { useState } from "react"
import Link from "next/link"
import { useRouter } from "next/navigation"

import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Checkbox } from "@/components/ui/checkbox"
import { Alert, AlertDescription } from "@/components/ui/alert"

import {
  EyeIcon,
  EyeOffIcon,
  GraduationCap,
  Users,
  AlertCircle,
} from "lucide-react"

import { login } from "@/lib/api" // ✅ REAL BACKEND API

export default function Login() {
  const [showPassword, setShowPassword] = useState(false)
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [error, setError] = useState("")
  const [isLoading, setIsLoading] = useState(false)

  const router = useRouter()

  // ============================
  // ✅ REAL LOGIN SUBMIT HANDLER
  // ============================
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError("")
    setIsLoading(true)

    try {
      const result = await login(email, password)

      console.log("LOGIN SUCCESS:", result)

      // ✅ ANY 200 RESPONSE = SUCCESS
      router.push("/dashboard")

    } catch (err: any) {
      console.error("LOGIN ERROR:", err)

      setError(
        err?.message ||
        "Invalid email or password"
      )
    } finally {
      setIsLoading(false)
    }
  }

  // demo buttons
  const fillDemoCredentials = (type: "student" | "professor") => {
    if (type === "student") {
      setEmail("danielle.johnson@bowiestate.edu")
      setPassword("Bowie@123")
    } else {
      setEmail("jeffrey.doyle@bowiestate.edu")
      setPassword("Bowie@123")
    }
    setError("")
  }

  return (
    <div className="flex min-h-screen bg-gray-50">
      <div className="flex flex-1 flex-col justify-center py-12 px-4 sm:px-6 lg:px-8">
        <div className="mx-auto w-full max-w-md">

          <div className="text-center mb-8">
            <h1 className="text-3xl font-bold text-gray-900">Welcome Back</h1>
            <p className="mt-2 text-gray-600">Sign in to access your account</p>
          </div>

          {/* DEMO BUTTONS */}
          <Card className="mb-6">
            <CardHeader>
              <CardTitle className="text-lg">Demo Login</CardTitle>
              <CardDescription>Auto-fill credentials</CardDescription>
            </CardHeader>
            <CardContent className="grid grid-cols-2 gap-3">
              <Button variant="outline" onClick={() => fillDemoCredentials("student")}>
                <GraduationCap className="mr-2 h-4 w-4" />
                Student
              </Button>
              <Button variant="outline" onClick={() => fillDemoCredentials("professor")}>
                <Users className="mr-2 h-4 w-4" />
                Faculty
              </Button>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Login</CardTitle>
              <CardDescription>Enter your credentials</CardDescription>
            </CardHeader>

            <CardContent>
              {error && (
                <Alert variant="destructive" className="mb-4">
                  <AlertCircle className="h-4 w-4" />
                  <AlertDescription>{error}</AlertDescription>
                </Alert>
              )}

              <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                  <Label>Email</Label>
                  <Input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                  />
                </div>

                <div>
                  <Label>Password</Label>
                  <div className="relative">
                    <Input
                      type={showPassword ? "text" : "password"}
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                      required
                    />
                    <button
                      type="button"
                      className="absolute right-3 top-1/2 -translate-y-1/2"
                      onClick={() => setShowPassword(!showPassword)}
                    >
                      {showPassword ? <EyeOffIcon /> : <EyeIcon />}
                    </button>
                  </div>
                </div>

                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <Checkbox />
                    <span className="text-sm">Remember me</span>
                  </div>
                  <Link href="/forgot-password" className="text-sm text-blue-600">
                    Forgot password?
                  </Link>
                </div>

                <Button type="submit" className="w-full" disabled={isLoading}>
                  {isLoading ? "Signing in..." : "Sign in"}
                </Button>
              </form>
            </CardContent>

            <CardFooter className="text-sm text-center">
              <span>
                Don’t have an account?{" "}
                <Link href="/signup" className="text-blue-600">
                  Sign up
                </Link>
              </span>
            </CardFooter>
          </Card>
        </div>
      </div>
    </div>
  )
}
