import grpc
# from . import bible_service_pb2 as bible_pb2
# from . import bible_service_pb2_grpc as bible_pb2_grpc

import bible_service_pb2 as bible_pb2
import bible_service_pb2_grpc as bible_pb2_grpc


def main():
    channel = grpc.insecure_channel('localhost:50052')  # Replace with your server address
    stub = bible_pb2_grpc.BibleServiceStub(channel)

    try:
        # Call the GetBibleVersions method
        response = stub.GetBibleVersions(bible_pb2.EmptyRequest())
        print("Bible Versions:", response.versions)

        # Call the GetBooksInVersion method
        version_request = bible_pb2.BibleVersionRequest(version="NIV")
        books_response = stub.GetBooksInVersion(version_request)
        print("Books in NIV version:", books_response.books)

        # Call the GetChaptersInBook method
        chapter_request = bible_pb2.BibleChapterRequest(version="NIV", book="Genesis")
        chapters_response = stub.GetChaptersInBook(chapter_request)
        print("Chapters in Genesis:", chapters_response.chapters)

        # Call the GetVerseInChapter method
        verse_request = bible_pb2.BibleVerseRequest(version="NIV", book="Genesis", chapter=1, verse=1)
        verse_response = stub.GetVerseInChapter(verse_request)
        print("Verse 1:1 in Genesis:", verse_response.content)

        # Call the CompareVerses method
        compare_request = bible_pb2.CompareVersesRequest(
            versions=["NIV", "KJV"], book="John", chapter=3, verse=16
        )
        compare_response = stub.CompareVerses(compare_request)
        for version, content in compare_response.verses.items():
            print(f"{version}: {content}")

    except grpc.RpcError as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
