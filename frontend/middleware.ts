import { withAuth } from "next-auth/middleware";

// Protect specific routes
export default withAuth({
  pages: {
    signIn: "/", // redirect here if not logged in
  },
});

// Specify which routes are protected
export const config = {
  matcher: ["/profile"],
};
