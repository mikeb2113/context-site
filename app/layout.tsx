import "./globals.css";
import Image from "next/image";
import Link from "next/link";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-neutral-950 text-neutral-100">
<header className="bg-[#1f1f1f] border-b border-neutral-800">
  <div className="relative mx-auto max-w-6xl px-5 h-14 flex items-center">
    
    {/* Centered title */}
    <Link
      href="/"
      className="absolute left-1/2 -translate-x-1/2 text-[#ce7807] text-4xl font-semibold tracking-tight"
    >
      {"{Context: }"}
    </Link>

    {/* Nav aligned right */}
    <nav className="ml-auto flex gap-10 text-sm text-[#ce7807]">
      <Link href="/example" className="opacity-80 hover:opacity-100">Example</Link>
      <Link href="/technical" className="opacity-80 hover:opacity-100">Technical</Link>
      <Link href="/try" className="opacity-80 hover:opacity-100">Try it</Link>
    </nav>

  </div>
</header>

        <main className="mx-auto max-w-6xl px-5 py-10">{children}</main>
      </body>
    </html>
  );
}