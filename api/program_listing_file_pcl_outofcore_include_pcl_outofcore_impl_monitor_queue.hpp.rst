
.. _program_listing_file_pcl_outofcore_include_pcl_outofcore_impl_monitor_queue.hpp:

Program Listing for File monitor_queue.hpp
==========================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_outofcore_include_pcl_outofcore_impl_monitor_queue.hpp>` (``pcl\outofcore\include\pcl\outofcore\impl\monitor_queue.hpp``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   //http://www.paulbridger.com/monitor_object/#ixzz2CeN1rr4P
   
   #ifndef PCL_OUTOFCORE_MONITOR_QUEUE_IMPL_H_
   #define PCL_OUTOFCORE_MONITOR_QUEUE_IMPL_H_
   
   #include <queue>
   
   template<typename DataT>
   class MonitorQueue : boost::noncopyable
   {
   public:
     void
     push (const DataT& newData)
     {
       boost::mutex::scoped_lock lock (monitor_mutex_);
       queue_.push (newData);
       item_available_.notify_one ();
     }
   
     DataT
     pop ()
     {
       boost::mutex::scoped_lock lock (monitor_mutex_);
   
       if (queue_.empty ())
       {
         item_available_.wait (lock);
       }
   
       DataT temp (queue_.front ());
       queue_.pop ();
   
       return temp;
     }
   
   private:
     std::queue<DataT> queue_;
     boost::mutex monitor_mutex_;
     boost::condition item_available_;
   };
   
   #endif //PCL_OUTOFCORE_MONITOR_QUEUE_IMPL_H_
