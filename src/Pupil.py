class Pupil:
      def request_book(self):
            print("Enter the name of the book you'd like to borrow>>")
            self.book=input()
            return self.book

      def return_book(self):
            print("Enter the name of the book you'd like to return>>")
            self.book=input()
            return self.book