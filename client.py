import grpc
from mygrpcapp import bible_pb2
from mygrpcapp import bible_pb2_grpc




# import grpc
# from bible_service_pb2 import (
#     BibleVersionListRequest,
#     BibleBookListRequest,
#     BibleChapterListRequest,
#     BibleVerseListRequest,
#     VerseRequest,
# )
# from bible_service_pb2_grpc import BibleServiceStub

# def main():
#     # Connect to the gRPC server running on localhost and port 50051 (adjust as needed)
#     channel = grpc.insecure_channel('localhost:50051')
#     stub = BibleServiceStub(channel)

#     # Example: Get a list of Bible versions
#     versions_request = BibleVersionListRequest()
#     versions_response = stub.GetBibleVersions(versions_request)
#     print("Available Bible Versions:")
#     for version in versions_response.versions:
#         print(version)

#     # Example: Get a list of books in a specific Bible version (ENGLISHAMP is the default)
#     books_request = BibleBookListRequest(version="ENGLISHAMP")
#     books_response = stub.GetBooksInVersion(books_request)
#     print(f"Books in {books_request.version}:")
#     for book in books_response.books:
#         print(book)

#     # Add more gRPC method calls here as needed...

#     # Example: Get a specific verse
#     verse_request = VerseRequest(version="ENGLISHAMP", book="John", chapter=3, verse=16)
#     verse_response = stub.GetVerse(verse_request)
#     print(f"John 3:16 - {verse_response.content}")

# if __name__ == '__main__':
#     main()


with grpc.insecure_channel('localhost:50051') as channel:
    stub = bible_pb2_grpc.BibleServiceStub(channel)
    response = stub.GetVerse(bible_pb2.GetVerseRequest(version="ENGLISHAMP", book="John", chapter=3, verse=16))
    print(response.content)

